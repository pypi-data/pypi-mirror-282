#pragma once
#include "dspedal/signal.h"

namespace dspedal
{
    template <typename T, typename CT = uint8_t>
    class Dff : public Signal<T>
    {
    public:
        Dff(Signal<CT> &clk, T initial = 0) : Signal<T>(initial), clk(clk)
        {
            next_state = initial;
        }

        virtual void eval_step()
        {
            if (clk.posedge())
            {
                next_state = *this->d;
            }
        }

        virtual void eval_end_step()
        {
            this->last = this->q;

            // Sync the output
            this->q = next_state;

            // Update output ports.
            for (auto o : this->driven_ports)
            {
                *o = this->q;
            }
        }

        // Signal interface
        // Implicit cast.
        operator const T() const
        {
            return this->read();
        }

        explicit operator int32_t() const
        {
            return this->read();
        }
        // assignment
        Signal<T> &operator=(const T &other)
        {
            this->write(other);
            return *this;
        }

        Signal<T> &operator=(const Signal<T> &other)
        {
            this->write(other.read());
            *this;
        }

    protected:
        Signal<CT> &clk;
        T next_state;
    };
} // namespace dspedal
