#pragma once
#include "dspedal/model.h"

#include <verilated.h>
#include <verilated_vcd_c.h>
// #include <verilated_fst_c.h>

namespace dspedal
{
    template <typename TraceType>
    class Tracer : public Model
    {
    public:
        std::unique_ptr<TraceType> tfp;

        Tracer(const std::string &trace_name, int levels, int options = 0) : Model(), tfp(std::make_unique<TraceType>())
        {
            context()->vcontext->traceEverOn(true);
            tfp->set_time_resolution("ns");
            tfp->set_time_unit("ns");

            context()->vcontext->trace(tfp.get(), levels, options);
            tfp->open(trace_name.c_str());
        }

        void eval_end_step(void)
        {
            tfp->dump(context()->time());
        }

        void close()
        {
            tfp->close();
        }
    };
} // dspedal
