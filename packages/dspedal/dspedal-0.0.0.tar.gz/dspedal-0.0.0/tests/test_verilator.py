from dspedal.verilator import VModule
from pathlib import Path
import dspedal


def test_verilator_module():
    """"""
    skid_source = dspedal.hdl_dir() / "skid.sv"

    mod = VModule.from_file(skid_source, "-GDW=23")
    print(mod)
