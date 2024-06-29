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


def verilator(*args: str, **kwargs: str):
    """Run verilator with given args."""
    vcmd = ["verilator", *args]
    # Add "--" flag for keyword args and flatten into a list.
    kargs = [x for xs in [[f"--{k}", str(v)] for k, v in kwargs.items()] for x in xs]
    vcmd.extend(kargs)
    subprocess.run(vcmd, check=True)


@dataclass
class VTypeTable:
    name: str
    typename: str
    range: str


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


def load_typetable(content) -> dict[str, VTypeTable]:
    """"""
    x = content["miscsp"][0]["typesp"]
    typetable = dict()

    for t in x:
        r = t["range"] if "range" in t.keys() else "0:0"
        typetable[t["addr"]] = VTypeTable(t["name"], t["type"], r)
    return typetable


def range_to_width(bitrange: str) -> int:
    """"""
    upper, lower = bitrange.strip().split(":")
    width = int(upper) - int(lower) + 1
    return width


def param_value(vstr: str):
    """"""
    split_str = "'sh" if "'sh" in vstr else "'h"
    _, hexcode = vstr.split(split_str)
    return int(hexcode, base=16)


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
            verilator(source_file, "--json-only", "--quiet", *verilator_args, Mdir=tdir)
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
            if x["varType"] == "GPARAM":
                val = param_value(x["valuep"][0]["name"])
                params.append(VParam(x["name"], dtype, width, val))
            elif x["varType"] == "PORT":
                dir = x["direction"].lower()
                ports.append(VPort(pname, dtype, width, dir))
        return cls(name, params, ports)


model_template = """
/*
    Generated using dspedal.generate.generate_vmodel
*/
#pragma once

#include "dspedal/dspedal.h"
#include "dspedal/vmodel.h"
#include "dspedal/bindings.h"

#include <nanobind/nanobind.h>

#include <${prefix}.h>

class ${name} : public dspedal::VModel<${prefix}, ${trace_type}>
{
protected:
    using dspedal::VModel<${prefix}, ${trace_type}>::top;

public:
    // Parameters
    ${parameters}

    // Connect using signals. Generated.
    ${name}(
        ${port_args})
        : dspedal::VModel<${prefix}, ${trace_type}>()
    {
        ${port_binds}
    }

    ${bus_constructor}
};

inline nanobind::class_<${name}, dspedal::Model> create_${name}(nanobind::handle &scope, const char *name)
{
    return dspedal::bind_model<${name}>(scope, name)
        .def(nanobind::init<
                ${binding_init}>(),
             ${binding_args})
        ${binding_params}
        .def("trace", &${name}::trace, nanobind::arg("trace_name"), nanobind::arg("levels") = 99);
}
"""


def stdintsize(n: int):
    """Round up to nearest stdint size"""
    base = math.ceil(math.log2(n)) if n > 8 else 3
    return int(2**base)


def cparam_member(param: VParam):
    """"""
    return f"const uint{stdintsize(param.width)}_t {param.name} = {param.default};"


def vport_args(port: VPort):
    """"""
    return f"dspedal::Signal<uint{stdintsize(port.width)}_t> &{port.name}"


def vport_bind(port: VPort):
    """"""
    return f'{port.name}.bind(&top->{port.name}, "{port.dir}");'


def binding_init(port: VPort):
    """"""
    return f"dspedal::Signal<uint{stdintsize(port.width)}_t> &"


def binding_arg(port: VPort):
    """"""
    return f'nanobind::arg("{port.name}")'


def binding_param(module: VModule, param: VParam):
    """Bind parameters as read-only field."""
    return f'.def_ro("{param.name}", &{module.name}::{param.name})'


def identify_axis(module: VModule):
    """"""
    # If "tdata" exists, it's a stream signal.
    tdata_signals = [p.name for p in module.ports if p.name.endswith("_tdata")]
    prefixes = [s.split("_tdata")[0] for s in tdata_signals]
    busses: dict[str, list[VPort]] = {}
    for prefix in prefixes:
        # Find other signals with prefix.
        tdata_count = 0
        tvalid_count = 0
        tready_count = 0
        bus_signals = [s for s in module.ports if s.name.startswith(prefix)]
        if len(bus_signals) != 3:
            raise Exception(
                f"Axis bus: {prefix} in module: {module.name} has {len(bus_signals)} signals. Requires 3."
            )
        for s in bus_signals:
            if s.name.endswith("tdata"):
                tdata_count += 1
            if s.name.endswith("tvalid"):
                tvalid_count += 1
            if s.name.endswith("tready"):
                tready_count += 1
        if tdata_count != 1 or tvalid_count != 1 or tready_count != 1:
            raise Exception(
                f"Axis bus: {prefix} in module: {module.name} has incorrect signal suffixes."
            )
        busses[prefix] = bus_signals
    return busses


def identify_busses(module: VModule):
    """Identify standard busses used in ports. AXIS, AXI-Lite, Wishbone."""
    busses: dict[str, dict[str, VPort]] = {}
    axis_busses = identify_axis(module)
    if len(axis_busses):
        busses["axis"] = axis_busses
    return busses


"""
Skid(
    dspedal::Signal<uint8_t> &clk,
    dspedal::Signal<uint8_t> &rst,
    Axis<uint32_t> &s_axis,
    Axis<uint32_t> &m_axis)
    : Skid(clk, rst, s_axis.tdata, s_axis.tvalid, s_axis.tready, m_axis.tdata, m_axis.tvalid, m_axis.tready)
{
}
"""


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
    busses = identify_busses(mod)
    bus_signals: list[VPort] = []
    for bus in busses.values():
        for bus_prefix, bus_ports in bus.items():
            bus_signals.extend(bus_ports)

    bus_signal_names = [s.name for s in bus_signals]
    non_busses: list[VPort] = []
    for p in mod.ports:
        if p.name not in bus_signal_names:
            non_busses.append(p)
    print(busses)
    print(non_busses)

    trace_type = "VerilatedFstC" if "--trace-fst" in verilator_args else "VerilatedVcdC"

    cparams_str = "\n\t".join([cparam_member(p) for p in mod.params])
    port_args_str = ",\n\t\t".join([vport_args(p) for p in mod.ports])
    port_binds_str = "\n\t\t".join([vport_bind(p) for p in mod.ports])
    bind_inits_str = ",\n\t\t".join([binding_init(p) for p in mod.ports])
    bind_args_str = ",\n\t\t".join([binding_arg(p) for p in mod.ports])
    bind_params_str = "\n\t\t".join([binding_param(mod, p) for p in mod.params])

    # Create the pymodule template based on the configuration
    vmodule = Template(model_template).safe_substitute(
        name=source_file.stem,
        prefix=prefix,
        trace_type=trace_type,
        parameters=cparams_str,
        port_args=port_args_str,
        port_binds=port_binds_str,
        binding_init=bind_inits_str,
        binding_args=bind_args_str,
        binding_params=bind_params_str,
        bus_constructor="",
    )
    with open(output_file, "w") as fp:
        fp.write(vmodule)


def generate_nb_module():
    """"""


# Command line arguments
class Args:
    source: Path
    output_directory: Path
    include_dirs: list[Path]
    prefix: str
    trace_fst: bool


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
    parser.add_argument("--trace_fst", action="store_true", help="Enable FST tracing.")

    args, verilator_args = parser.parse_known_args()
    args: Args

    # Verilated model name
    prefix = f"V{args.source.stem}" if args.prefix is None else args.prefix

    # Append include dirs to verilator args
    include_args = [f"-I{d.absolute()}" for d in args.include_dirs]
    verilator_args.extend(include_args)
    verilator_args.extend(["--prefix", prefix])
    if args.trace_fst:
        verilator_args.append("--trace-fst")
    else:
        verilator_args.append("--trace")
    # Create output directory
    args.output_directory.mkdir(exist_ok=True)
    # Generate the binding header.
    output_file = (args.output_directory / args.source.stem).with_suffix(".h")
    generate_vmodel(args.source, output_file, prefix, *verilator_args)


if __name__ == "__main__":
    main()
