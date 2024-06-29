#pragma once
#include "dspedal/model.h"
#include "dspedal/signal.h"

#include <verilated.h>
#include <verilated_vcd_c.h>
#include <verilated_fst_c.h>

namespace dspedal
{
    template <typename V, typename TraceType = VerilatedFstC>
    class VModel : public Model
    {
    protected:
        // Internal verilated model.
        std::unique_ptr<VerilatedContext> vcontext;
        std::unique_ptr<V> top;
        std::unique_ptr<TraceType> tfp;

    public:
        VModel()
            : Model(),
              vcontext(std::make_unique<VerilatedContext>()),
              top(std::make_unique<V>(vcontext.get()))
        {
        }

        void trace(const std::string &trace_name, int levels = 99)
        {
            // Verilated::traceEverOn(true);
            vcontext->traceEverOn(true);
            tfp = std::make_unique<TraceType>();
            tfp->set_time_resolution("ns");
            tfp->set_time_unit("ns");

            top->trace(tfp.get(), levels);

            tfp->open(trace_name.c_str());
        }

        virtual void eval_step()
        {
            top->eval_step();
        }

        virtual void eval_end_step()
        {
            top->eval_end_step();
            if (tfp)
            {
                tfp->dump(context()->time());
            }
        }
    };
} // namespace dspedal
