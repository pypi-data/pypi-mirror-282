from argparse import ArgumentParser
import dspedal
from dataclasses import dataclass
from pathlib import Path

import dspedal.generate


@dataclass
class DSPedalArgs:
    version: bool
    cmake_dir: bool
    include_dir: bool
    hdl_dir: bool


def exec_dspedal(args: DSPedalArgs, unknown_args):
    """"""
    print("DSPedal Func")
    if args.cmake_dir:
        print(dspedal.cmake_dir())
    if args.include_dir:
        print(dspedal.include_dir())
    if args.hdl_dir:
        print(dspedal.hdl_dir())


@dataclass
class GenerateArgs:
    source_file: Path
    output_dir: Path


def exec_generate(args: GenerateArgs, verilator_args: list[str]):
    """"""
    print("Generate Function")
    print(f"Source: {args.source_file.absolute()}")
    print(f"Output: {args.output_dir.absolute()}")
    print(f"Vargs: {verilator_args}")

    name = args.source_file.stem
    output_file = args.output_dir / f"{name}.h"

    dspedal.generate.generate_vmodel(args.source_file, output_file, *verilator_args)


parser = ArgumentParser("dspedal")
parser.add_argument("--version", action="version", version=dspedal.__version__)
parser.add_argument("--cmake_dir", action="store_true")
parser.add_argument("--include_dir", action="store_true")
parser.add_argument("--hdl_dir", action="store_true")
parser.set_defaults(func=exec_dspedal)
subparsers = parser.add_subparsers()

generate_parser = subparsers.add_parser("generate")
generate_parser.add_argument("source_file", type=Path, help="Verilog source file.")
generate_parser.add_argument("--output_dir", type=Path, default=Path())
# generate_parser.add_argument("--verilator_args", nargs="*", help="Verilator args.")
generate_parser.set_defaults(func=exec_generate)


def main():
    """"""
    args, unknown_args = parser.parse_known_args()
    args.func(args, unknown_args)


if __name__ == "__main__":
    main()
