from pathlib import Path

__version__ = "0.0.0"


def hdl_dir():
    """"""
    return Path(__file__).parent / "hdl"


def cmake_dir():
    """"""
    return Path(__file__).parent / "cmake"


def include_dir():
    """"""
    return Path(__file__).parent / "include"
