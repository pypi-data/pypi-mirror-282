#include "dspedal/dspedal.h"
#include "dspedal/bindings.h"

using namespace dspedal;
namespace nb = nanobind;

NB_MODULE(_framework, m)
{
      bind_module_context(m);

      bind_context(m, "Context");
      bind_base_model(m, "Model");
      m.def("clear_context", []()
            { Model::context()->clear(); });

      // Signals
      bind_signal<uint8_t>(m, "Signal8");
      bind_signal<uint16_t>(m, "Signal16");
      bind_signal<uint32_t>(m, "Signal32");
      bind_dff<uint8_t>(m, "Dff8");
      bind_dff<uint16_t>(m, "Dff16");
      bind_dff<uint32_t>(m, "Dff32");

      // Clock
      bind_clock(m, "Clock");

      // AXI Busses.
      bind_axis<uint8_t>(m, "Axis8");
      bind_axis<uint16_t>(m, "Axis16");
      bind_axis<uint32_t>(m, "Axis32");

      // AXIS Drivers
      bind_axis_tx<uint8_t>(m, "AxisTx8");
      bind_axis_tx<uint16_t>(m, "AxisTx16");
      bind_axis_tx<uint32_t>(m, "AxisTx32");

      bind_axis_rx<uint8_t>(m, "AxisRx8");
      bind_axis_rx<uint16_t>(m, "AxisRx16");
      bind_axis_rx<uint32_t>(m, "AxisRx32");

      // Simulator
      bind_simulator(m, "Simulator");

      // // Framework models
      // create_Skid(m);
}
