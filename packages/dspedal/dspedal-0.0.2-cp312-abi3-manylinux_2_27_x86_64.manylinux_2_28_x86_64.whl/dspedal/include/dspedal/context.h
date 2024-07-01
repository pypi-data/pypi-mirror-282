#pragma once

#include <cstdint>
#include <list>
#include <memory>
#include <verilated.h>

namespace dspedal
{
    // Forward declaration of the model class.
    class Model;

    /*
        The context will maintain a list of all models that must be evaluated.
        It also contains the time used across all models.
    */
    class Context
    {
    public:
        std::unique_ptr<VerilatedContext> vcontext;

        Context() : vcontext(std::make_unique<VerilatedContext>())
        {
        }

        // Clear models from the list and reset the clock.
        void clear(void)
        {
            m_models.clear();
            vcontext = std::make_unique<VerilatedContext>();
        }

        // Register a model for evaluation with this context.
        void register_model(Model *model)
        {
            m_models.push_back(model);
        }

        // Get current context time.
        uint64_t time(void)
        {
            return vcontext->time();
        }

        // Increment the time by the given step.
        void time_inc(uint64_t time_step)
        {
            vcontext->timeInc(time_step);
        }

        std::list<Model *> &models()
        {
            return m_models;
        }

    public:
        std::list<Model *> m_models;
    };

    using ContextPtr = Context *;
} // namespace dspedal
