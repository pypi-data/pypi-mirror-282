#!/usr/bin/env python3
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
    VcdTracer,
)

from dspedal.library import Skid, Gain, IIR
import numpy as np


def main():
    """"""
    clear_context()

    clk = Clock(10)
    rst = Dff8(clk, 1)

    bus0 = Axis32()
    bus1 = Axis32()
    bus2 = Axis32()
    bus3 = Axis32()

    axis_tx = AxisTx32(clk, rst, bus0)
    axis_rx = AxisRx32(clk, rst, bus3)

    # IIR Filter
    iir_coefs = [Signal32(i) for i in range(6)]
    iir = IIR(clk, rst, bus0, bus1, iir_coefs)

    # Skid buffer
    skid = Skid(clk, rst, bus1, bus2)

    # Gain
    k = Signal32(65536)
    gain = Gain(clk, rst, bus2, bus3, k)

    # Trace.
    tracer = VcdTracer("traces/some_trace.vcd", 1)

    sim = Simulator()

    sim.reset(rst, 100)
    sim.advance(100)

    tx_data = np.array([31, 32, 33, 34])
    axis_tx.write(tx_data)

    sim.advance(100)
    axis_rx.tready = 1
    sim.advance(100)

    rx_data = axis_rx.read()
    print(rx_data)
    assert np.all(rx_data == tx_data)

    # tracer.close()


if __name__ == "__main__":
    main()
