#include "dspedal/dspedal.h"
#include "dspedal/vmodel.h"

#include <VSkid.h>
#include <catch2/catch_test_macros.hpp>

using namespace dspedal;

template <typename V, typename TraceType = VerilatedVcdC>
class Skid : public VModel<V, TraceType>
{
protected:
    using VModel<V, TraceType>::top;

public:
    // Connect using signals. Generated.
    Skid(
        Signal<uint8_t> &clk,
        Signal<uint8_t> &rst,
        Signal<uint32_t> &s_axis_tdata,
        Signal<uint8_t> &s_axis_tvalid,
        Signal<uint8_t> &s_axis_tready,
        Signal<uint32_t> &m_axis_tdata,
        Signal<uint8_t> &m_axis_tvalid,
        Signal<uint8_t> &m_axis_tready)
        : VModel<V, TraceType>()
    {
        clk.bind(&top->clk, "input");
        rst.bind(&top->rst, "input");
        s_axis_tdata.bind(&top->s_axis_tdata, "input");
        s_axis_tvalid.bind(&top->s_axis_tvalid, "input");
        s_axis_tready.bind(&top->s_axis_tready, "output");
        m_axis_tdata.bind(&top->m_axis_tdata, "output");
        m_axis_tvalid.bind(&top->m_axis_tvalid, "output");
        m_axis_tready.bind(&top->m_axis_tready, "input");
    }

    // Connect using busses.
    Skid(Signal<uint8_t> &clk,
         Signal<uint8_t> &rst,
         Axis<uint32_t> &s_axis,
         Axis<uint32_t> &m_axis)
        : Skid(clk, rst, s_axis.tdata, s_axis.tvalid, s_axis.tready, m_axis.tdata, m_axis.tvalid, m_axis.tready)
    {
    }
};

TEST_CASE("Context")
{
    Model::context()->clear();

    // Declare signals and busses.
    auto clk = Clock<uint8_t>(10);
    auto rst = Dff<uint8_t>(clk, 1);
    auto bus0 = Axis<uint32_t>();
    auto bus1 = Axis<uint32_t>();

    // Models
    auto axis_tx = AxisTx<uint32_t>(clk, rst, bus0);

    auto some_model = Skid<VSkid, VerilatedFstC>(clk, rst, bus0, bus1);
    some_model.trace("context.fst");

    auto axis_rx = AxisRx<uint32_t>(clk, rst, bus1);

    REQUIRE(Model::context()->models.size() == 11);

    auto sim = Simulator();

    sim.reset(rst);

    sim.advance(100);

    axis_tx.write({1, 2, 3, 4});

    sim.advance(100);

    axis_rx.tready(1);

    sim.advance(100);

    auto rx_data = axis_rx.read();
    REQUIRE(rx_data == std::vector<uint32_t>{1, 2, 3, 4});
}
