#pragma once
#include "dspedal/model.h"
#include <verilated.h>

namespace dspedal
{
    template <typename V>
    class VModel : public Model
    {
    protected:
        // Internal verilated model.
        std::unique_ptr<V> top;

    public:
        VModel() : Model()
        {
            top = std::make_unique<V>(context()->vcontext.get());
        }

        void eval_step()
        {
            top->eval_step();
        }

        void eval_end_step()
        {
            top->eval_end_step();
        }
    };
} // namespace dspedal
