#!/usr/bin/env python3

import subprocess
from pathlib import Path
import shutil
import argparse
import nanobind


class Args(argparse.Namespace):
    cmake: bool = False
    clean: bool = False
    build_dir: Path = Path("build")
    config: str = "Release"
    target: str = "run_all_tests"
    compiler: str = "clang"
    generator: str = "Ninja"
    nanobind: str = nanobind.cmake_dir()


compiler_options = {
    "gcc": (Path("/usr/bin/gcc"), Path("/usr/bin/g++")),
    "clang": (Path("/usr/bin/clang"), Path("/usr/bin/clang++")),
}

parser = argparse.ArgumentParser()
parser.add_argument("--cmake", action="store_true")
parser.add_argument("--clean", action="store_true")
parser.add_argument("-build_dir", action="store", type=Path, default=Path("build"))
parser.add_argument("-config", action="store", type=str, default="Release")
parser.add_argument("-target", action="store", type=str, default="run_all_tests")
parser.add_argument("-compiler", action="store", type=str, default="clang")
parser.add_argument("-generator", action="store", type=str, default="Ninja")
parser.add_argument("-nanobind", action="store", type=str, default=nanobind.cmake_dir())


# parser.add_argument
def main():
    """"""
    args, test_args = parser.parse_known_args(namespace=Args)

    # Get the selected compiler.
    c_compiler, cxx_compiler = compiler_options[args.compiler]

    # Clean the build dir
    if args.clean:
        shutil.rmtree(args.build_dir, ignore_errors=True)

    cmake_cmd = [
        "cmake",
        "-S",
        Path(),
        "-B",
        args.build_dir,
        "-G",
        args.generator,
        f"-Dnanobind_DIR={args.nanobind}",
        # f"-DCMAKE_C_COMPILER={c_compiler}",
        f"-DCMAKE_CXX_COMPILER={cxx_compiler}",
        f"-DCMAKE_BUILD_TYPE={args.config}",
    ]
    if args.cmake:
        subprocess.run(cmake_cmd, check=True)

    build_cmd = [
        "cmake",
        "--build",
        args.build_dir,
        "--config",
        args.config,
        "--target",
        args.target,
    ]
    subprocess.run(build_cmd, check=True)

    run_cmd = ["ctest", "--test-dir", args.build_dir, "--output-on-failure"]
    if len(test_args) > 0:
        run_cmd.append("-R")
        run_cmd.append("|".join(test_args))

    subprocess.run(run_cmd, check=False)


if __name__ == "__main__":
    main()
