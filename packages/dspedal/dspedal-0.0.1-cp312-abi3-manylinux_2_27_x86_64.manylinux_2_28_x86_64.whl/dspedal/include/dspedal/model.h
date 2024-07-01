#pragma once
#include "dspedal/context.h"

namespace dspedal
{
    class Model
    {
    public:
        // ContextPtr context;

        Model()
        {
            // Models will self-register to the global context.
            context()->register_model(this);
        }

        virtual void eval_step() {}
        virtual void eval_end_step() {}

        static ContextPtr context(ContextPtr new_context = nullptr)
        {
            static Context global_context;
            static ContextPtr m_context = &global_context;

            if (new_context)
            {
                m_context = new_context;
            }

            return m_context;
        }

        //
        void set_context(ContextPtr new_context)
        {
            context(new_context);
        }
        ContextPtr get_context()
        {
            return context();
        }
    };
} // namespace dspedal
