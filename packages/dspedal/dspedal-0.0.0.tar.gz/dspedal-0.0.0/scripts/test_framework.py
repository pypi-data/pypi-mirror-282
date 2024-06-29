from dspedal.framework import (
    Context,
    Model,
    Clock,
    Signal8,
    Signal16,
    Signal32,
    Dff8,
    Dff16,
    Dff32,
    Axis32,
    Simulator,
    AxisTx32,
    AxisRx32,
    clear_context,
)

from dspedal.library import SomeModel, Skid
import numpy as np


def main():
    """"""
    clear_context()
    clk = Clock(10)
    rst = Dff8(clk, 1)

    bus0 = Axis32()
    bus1 = Axis32()

    axis_tx = AxisTx32(clk, rst, bus0)
    axis_rx = AxisRx32(clk, rst, bus1)

    skid = Skid(
        clk,
        rst,
        bus0.tdata,
        bus0.tvalid,
        bus0.tready,
        bus1.tdata,
        bus1.tvalid,
        bus1.tready,
    )
    # some_model = SomeModel()
    skid.trace("traces/skid.fst")

    sim = Simulator()

    sim.reset(rst, 105)

    sim.advance(100)

    # s_axis.tdata.d = 43
    # s_axis.tvalid.d = 1
    # sim.advance(10)
    # s_axis.tvalid.d = 0
    # tx_data = [42, 43, 44, 54]
    tx_data = np.array([31, 32, 33, 34])
    axis_tx.write(tx_data)

    sim.advance(90)
    axis_rx.tready = 1
    sim.advance(100)

    rx_data = axis_rx.read()
    print(rx_data)
    assert np.all(rx_data == tx_data)


if __name__ == "__main__":
    main()
