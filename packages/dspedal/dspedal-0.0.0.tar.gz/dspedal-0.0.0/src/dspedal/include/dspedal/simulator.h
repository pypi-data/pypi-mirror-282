#pragma once
#include "dspedal/model.h"
#include "dspedal/signal.h"

namespace dspedal
{
    class Simulator
    {
    public:
        ContextPtr context;
        uint64_t time_step = 1;

        Simulator() : context(Model::context())
        {
        }

        void eval()
        {
            for (auto &m : context->models)
            {
                m->eval_step();
            }
            for (auto &m : context->models)
            {
                m->eval_end_step();
            }
        }

        void advance(int time_inc)
        {
            int n_steps = time_inc / time_step;
            for (int i = 0; i < n_steps; i++)
            {
                eval();
                // context->dump();
                context->time_inc(time_step);
            }
        }

        void reset(Signal<uint8_t> &rst, int duration = 100)
        {
            rst = 1;
            this->advance(duration);
            rst = 0;
        }

    public:
    };
} // namespace dspedal
