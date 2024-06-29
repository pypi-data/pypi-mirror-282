#pragma once
#include "dspedal/signal.h"

namespace dspedal
{
    template <typename T = uint8_t>
    class Clock : public Signal<T>
    {
    public:
        Clock(uint64_t period) : Signal<T>(), m_half_period(period / 2)
        {
            m_checkpoint = this->context()->time() + m_half_period;
            this->q = 1;
            *this->d = 1;
        }

        virtual void eval_step()
        {
            if (this->context()->time() >= m_checkpoint)
            {
                *this->d = !this->q;
                m_checkpoint += m_half_period;
            }
        }

        uint64_t period()
        {
            return m_half_period * 2;
        }

    protected:
        uint64_t m_half_period;
        uint64_t m_checkpoint;
    };
} // namespace dspedal
