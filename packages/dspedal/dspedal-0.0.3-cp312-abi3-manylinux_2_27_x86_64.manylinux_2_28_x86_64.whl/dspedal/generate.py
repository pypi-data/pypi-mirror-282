""""""

from pathlib import Path
import importlib.resources as pkg_resources
from string import Template
import subprocess
from dataclasses import dataclass, fields, field
import json
from tempfile import TemporaryDirectory
from argparse import ArgumentParser
import math
import os

model_template = Template(
    """
/*
    Generated using dspedal.generate.generate_vmodel
*/
#pragma once

#include "dspedal/dspedal.h"
#include "dspedal/vmodel.h"
#include "dspedal/bindings.h"

#include <nanobind/nanobind.h>

#include <${prefix}.h>

class ${name} : public dspedal::VModel<${prefix}>
{
protected:
    using dspedal::VModel<${prefix}>::top;

public:
    // Parameters
    ${cpp_params}

    // Connect using Signals.
    ${name}(${port_args}) : dspedal::VModel<${prefix}>()
    {
        ${connect_top}
    }

    // Connect using Busses (Axis, Wishbone, ...)
    ${bus_constructor}

    // Create nanobind binding.
    static inline auto create_binding(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<${name}>(scope, name)
            ${init_def}
            ${bus_init_def}
            ${nb_params}
            .def_prop_ro("context", &${name}::get_context, nanobind::sig("def context(self) -> dspedal.framework.Context"));
    }
};

"""
)


def verilator(*args: str, **kwargs: str):
    """Run verilator with given args."""
    verilator_root = os.getenv("VERILATOR_ROOT")
    if verilator_root is not None:
        verilator_bin = Path(verilator_root) / "bin/verilator_bin"
    else:
        # Assume it's on the path somewhere.
        verilator_bin = "verilator"

    print(f"verilator_bin: {verilator_bin}")
    vcmd = [verilator_bin, *args]
    # Add "--" flag for keyword args and flatten into a list.
    kargs = [x for xs in [[f"--{k}", str(v)] for k, v in kwargs.items()] for x in xs]
    vcmd.extend(kargs)
    subprocess.run(vcmd, check=True)


def range_to_width(bitrange: str) -> int:
    """Convert verilog range to a width."""
    upper, lower = bitrange.strip().split(":")
    width = int(upper) - int(lower) + 1
    return width


def param_value(vstr: str):
    """Convert parameter value in typetable to an integer"""
    split_str = "'sh" if "'sh" in vstr else "'h"
    _, hexcode = vstr.split(split_str)
    return int(hexcode, base=16)


def stdintsize(n: int):
    """Round up to nearest stdint size"""
    base = math.ceil(math.log2(n)) if n > 8 else 3
    return int(2**base)


@dataclass
class VTypeTable:
    name: str
    typename: str
    range: str
    arr_range: str = None


@dataclass
class VParam:
    name: str
    dtype: str
    width: int
    default: int | str


@dataclass
class VPort:
    name: str
    dtype: str
    width: int
    dir: str
    arr_range: int = None

    def cpparg(self, use_name: bool = True) -> str:
        """C++ format of this port."""
        arg_name = self.name if use_name else ""
        if self.arr_range:
            return f"std::array<dspedal::Signal<uint{stdintsize(self.width)}_t>*, {self.arr_range}> &{arg_name}"
        else:
            return f"dspedal::Signal<uint{stdintsize(self.width)}_t> &{arg_name}"

    def nbsig(self) -> str:
        """Nanobind signature"""
        if self.arr_range:
            return f"{self.name}: collections.abc.Sequence[dspedal.framework.Signal{stdintsize(self.width)}]"
        else:
            return f"{self.name}: dspedal.framework.Signal{stdintsize(self.width)}"

    def connect_top(self) -> str:
        """Connect port Signal's to verilated module's ports."""
        return f'dspedal::connect({self.name}, top->{self.name}, "{self.dir}");'


@dataclass
class AxisBus:
    name: str
    width: int
    dir: str

    def cpparg(self, use_name: bool = True) -> str:
        """C++ format of AXIS bus arg."""
        arg_name = self.name if use_name else ""
        return f"dspedal::Axis<uint{stdintsize(self.width)}_t> &{arg_name}"

    def nbsig(self) -> str:
        """Nanobind type signature"""
        return f"{self.name}: dspedal.framework.Axis{stdintsize(self.width)}"


@dataclass
class WishboneBus:
    name: str
    aw: int
    dw: int
    dir: str

    def cpparg(self, use_name: bool = True) -> str:
        """C++ format of AXIS bus arg."""
        arg_name = self.name if use_name else ""
        return f"dspedal::Wishbone<uint{stdintsize(self.aw)}_t, {stdintsize(self.dw)}> &{arg_name}"

    def nbsig(self) -> str:
        """Nanobind type signature"""
        return f"{self.name}: dspedal.framework.Wishbone{stdintsize(self.dw)}"


def load_typetable(content) -> dict[str, VTypeTable]:
    """"""
    x = content["miscsp"][0]["typesp"]
    typetable = dict()

    for t in x:
        # Array type
        if "declRange" in t.keys():
            refaddr = t["refDTypep"]
            for dtypes in x:
                if dtypes["addr"] == refaddr:
                    refrange = dtypes["range"]
                    reftype = dtypes["type"]
                    refname = dtypes["name"]
                    arr_range = str(t["declRange"]).replace("[", "").replace("]", "")
            typetable[t["addr"]] = VTypeTable(refname, t["type"], refrange, arr_range)
        else:
            r = t["range"] if "range" in t.keys() else "0:0"
            typetable[t["addr"]] = VTypeTable(t["name"], t["type"], r)
    return typetable


@dataclass
class VModule:
    name: str
    params: list[VParam]
    ports: list[VPort]

    @classmethod
    def from_file(cls, source_file: Path, *verilator_args: str):
        """Load module interface from source file."""

        # Enter a temporary directory
        with TemporaryDirectory() as tdir:
            # Run the verilator command to generate the json data.
            verilator(source_file, "--json-only", *verilator_args, Mdir=tdir)
            # Identify and load the json file.
            json_file = list(Path(tdir).glob("*.tree.json"))[0]
            with open(json_file) as fp:
                content = json.load(fp)
        # Get the typetable from the json data.
        typetable = load_typetable(content)

        # Load the module params and ports from the data.
        stmtsp = content["modulesp"][0]["stmtsp"]
        name = content["modulesp"][0]["name"]
        params = []
        ports = []

        for x in stmtsp:
            # print(x)
            if x["type"] != "VAR":
                continue
            pname = x["name"]
            width = range_to_width(typetable[x["dtypep"]].range)
            dtype = typetable[x["dtypep"]].name
            _arr_range_str = typetable[x["dtypep"]].arr_range
            arr_range = (
                range_to_width(_arr_range_str) if _arr_range_str is not None else None
            )

            if x["varType"] == "GPARAM":
                val = param_value(x["valuep"][0]["name"])
                params.append(VParam(x["name"], dtype, width, val))
            elif x["varType"] == "PORT":
                dir = x["direction"].lower()
                ports.append(VPort(pname, dtype, width, dir, arr_range))

        return cls(name, params, ports)

    def cpp_params(self) -> str:
        """Generate paramter definitions str for C++ model."""
        return "\n\t".join(
            [
                f"const uint{stdintsize(param.width)}_t {param.name} = {param.default};"
                for param in self.params
            ]
        )

    def cpp_ctor_args(self, use_name: bool = True) -> str:
        """Generate C++ constructor args. Skip using the variable name when used in a template like nanobind::init<>"""
        return ", ".join([port.cpparg(use_name) for port in self.ports])

    def cpp_bus_ctor_args(self, use_name: bool = True) -> str:
        """Bus constructor"""

    def _init_sig(self) -> str:
        """Nanobind constructor signature."""
        return f'nanobind::sig("def __init__(self, {", ".join([port.nbsig() for port in self.ports])}) -> None")'

    def init_def(self) -> str:
        """Primary Nanobind __init__ definition."""
        return (
            f".def(nanobind::init<{self.cpp_ctor_args(False)}>(), {self._init_sig()})"
        )

    def _bus_init_sig(self) -> str:
        """"""

    def bus_init_def(self) -> str:
        """"""

    def nb_params(self) -> str:
        return "\n\t\t\t".join(
            [
                f'.def_ro("{param.name}", &{self.name}::{param.name})'
                for param in self.params
            ]
        )

    def connect_top(self) -> str:
        """Return string to connect Signals to verilated top module's ports."""
        return "\n\t\t".join([port.connect_top() for port in self.ports])


def identify_axis(mod: VModule, port: VPort) -> AxisBus | None:
    """"""
    if port.name.endswith("_tdata"):
        suffix = "_tdata"
    elif port.name.endswith("_tvalid"):
        suffix = "_tvalid"
    elif port.name.endswith("_tready"):
        suffix = "_tready"
    else:
        return None

    prefix = port.name.split(suffix)[0]
    all_ports = {f"{p.name}": p for p in mod.ports}
    if f"{prefix}_tdata" in all_ports.keys():
        width = all_ports[f"{prefix}_tdata"].width
        dir = all_ports[f"{prefix}_tdata"].dir
    else:
        raise Exception(f"{prefix}_tdata not in ports list")
    return AxisBus(prefix, width, dir)


def identify_wishbone(mod: VModule, port: VPort) -> WishboneBus | None:
    """"""
    return None


def _identify_bus(mod: VModule, port: VPort) -> AxisBus | WishboneBus | None:
    """"""
    bus = identify_axis(mod, port)
    if bus is not None:
        return bus
    bus = identify_wishbone(mod, port)
    if bus is not None:
        return bus


def identify_busses(mod: VModule):
    """Identify standard busses used in ports. AXIS, AXI-Lite, Wishbone."""
    # busses: dict[str, tuple[str, int]] = {}  # signal_name: (bus_type, bus_width)
    busses: dict[str, VPort | AxisBus | WishboneBus] = {}
    # signal_busses: dict[str, str] = {}  # signal_name: (bus_name, suffix)
    signal_busses: dict[str, VPort] = {}

    for p in mod.ports:
        bus = _identify_bus(mod, p)
        if bus is None:
            signal_busses[p.name] = p.name
            busses[p.name] = p
        else:
            suffix = p.name.split(bus.name)[1].split("_")[1]
            signal_busses[p.name] = f"{bus.name}.{suffix}"
            busses[bus.name] = bus
            # print(prefix, bus_type, width)
    return busses, signal_busses


def generate_vmodel(
    source_file: Path,
    output_file: Path,
    prefix: str,
    *verilator_args: str,
):
    """"""
    print("Generating VModel")
    # Load the verilog module's config.
    mod = VModule.from_file(source_file, *verilator_args)
    busses, signal_busses = identify_busses(mod)
    # print(busses)
    # print(signal_busses)
    # exit()

    has_busses = len(busses) != len(mod.ports)
    if has_busses:
        base_ctor_args = ", ".join([x for x in signal_busses.values()])
        bus_ctor_args = ", ".join([b.cpparg(True) for b in busses.values()])
        bus_constructor = (
            f"{mod.name}({bus_ctor_args}) : {mod.name}({base_ctor_args}){{}}"
        )
        # bus_ctor_sig_str = f'nanobind::sig("def __init__(self, {", ".join([f"{n}: dspedal.framework.{t[0]}{stdintsize(t[1])}" for n,t in busses.items()])}) -> None")'
        # bus_ctor_bind_str = f".def(nanobind::init<{", ".join([f"dspedal::{t[0]}<uint{t[1]}_t> &" for t in busses.values()])}>(), {bus_ctor_sig_str})"
        bus_init_sig_args = ", ".join([b.nbsig() for b in busses.values()])
        bus_init_sig = (
            f'nanobind::sig("def __init__(self, {bus_init_sig_args}) -> None")'
        )
        bus_init_args = ", ".join([b.cpparg(False) for b in busses.values()])
        bus_init_def = f".def(nanobind::init<{bus_init_args}>(), {bus_init_sig})"

    else:
        bus_constructor = ""
        bus_init_def = ""

    # Create the pymodule template based on the configuration
    vmodule = model_template.safe_substitute(
        name=source_file.stem,
        prefix=prefix,
        cpp_params=mod.cpp_params(),
        port_args=mod.cpp_ctor_args(True),
        connect_top=mod.connect_top(),
        init_def=mod.init_def(),
        bus_constructor=bus_constructor,
        bus_init_def=bus_init_def,
        nb_params=mod.nb_params(),
    )
    with open(output_file, "w") as fp:
        fp.write(vmodule)


# Command line arguments
class Args:
    source: Path
    output_directory: Path
    include_dirs: list[Path]
    prefix: str


def main():
    """"""
    parser = ArgumentParser("DSPedal Model Bindings Generator.")
    parser.add_argument(
        "source",
        action="store",
        type=Path,
        help="Create models for given hdl source.",
    )
    parser.add_argument(
        "-output_directory",
        action="store",
        type=Path,
        default=Path("Generated"),
        help="Generated output directory.",
    )
    parser.add_argument(
        "-include_dirs",
        action="store",
        type=Path,
        default=[],
        nargs="*",
        help="HDL Include dirs.",
    )
    parser.add_argument("-prefix", type=str, default=None, help="Verilated model name.")

    args, verilator_args = parser.parse_known_args()
    args: Args

    # Verilated model name
    prefix = f"V{args.source.stem}" if args.prefix is None else args.prefix

    # Append include dirs to verilator args
    include_args = [f"-I{d.absolute()}" for d in args.include_dirs]
    verilator_args.extend(include_args)
    verilator_args.extend(["--prefix", prefix])
    # verilator_args.append("--trace")
    # Create output directory
    args.output_directory.mkdir(exist_ok=True)
    # Generate the binding header.
    output_file = (args.output_directory / args.source.stem).with_suffix(".h")
    generate_vmodel(args.source, output_file, prefix, *verilator_args)


if __name__ == "__main__":
    main()
