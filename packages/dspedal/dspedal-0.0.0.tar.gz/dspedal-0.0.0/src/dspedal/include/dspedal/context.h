#pragma once

#include <cstdint>
#include <list>
#include <memory>

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
        Context() : m_time(0)
        {
        }

        // Clear models from the list and reset the clock.
        void clear(void)
        {
            m_time = 0;
            models.clear();
        }

        // Register a model for evaluation with this context.
        void register_model(Model *model)
        {
            models.push_back(model);
        }

        // Get current context time.
        uint64_t time(void)
        {
            return m_time;
        }

        // Increment the time by the given step.
        void time_inc(uint64_t time_step)
        {
            m_time += time_step;
        }

    public:
        std::list<Model *> models;

    private:
        uint64_t m_time;
    };

    using ContextPtr = Context *;
} // namespace dspedal
