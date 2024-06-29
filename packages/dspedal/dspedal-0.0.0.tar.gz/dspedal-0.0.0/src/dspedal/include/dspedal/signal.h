#pragma once
#include "dspedal/model.h"

namespace dspedal
{
    template <typename T>
    class Signal : public Model
    {
    public:
        Signal(T initial = 0) : Model()
        {
            d = &d_local;
            *d = initial;
            q = initial;
            last = !initial; // Force edge change on first clock cycle.
        }

        virtual void eval_end_step()
        {
            last = q;
            // Sync the output
            q = *d;

            // Update output ports.
            for (auto o : driven_ports)
            {
                *o = q;
            }
        }

        // Bind a port to this signal.
        void bind(T *port, const std::string &direction)
        {
            if (direction.rfind("i", 0) == 0)
            {
                driven_ports.push_back(port);
                // Initialize the port value.
                *port = q;
            }
            else if (direction.rfind("o", 0) == 0)
            {
                // Link d pin to the output port.
                d = port;
            }
        }

        // Signal has transitioned from 0 to non-zero in the last evaluation cycle.
        bool posedge(void)
        {
            return q && !last;
        }

        // Signal has transitioned from non-zero to 0 in the last evaluation cycle.
        bool negedge(void)
        {
            return !q && last;
        }

        // If the signal has changed in the last evaluation cycle.
        bool changed(void)
        {
            return q != last;
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

        void write(const T value)
        {
            *d = value;
        }

        void writei(int value)
        {
            *d = value;
        }

        const T read() const
        {
            return q;
        }

        const T _read_d() const
        {
            return *d;
        }

    protected:
        T *d;      // Signal input.
        T d_local; // Local value of d if d is not bound.
        T q;       // Signal output.
        T last;    // Value from the last evaluation cycle.
        std::list<T *> driven_ports;
        bool m_posedge = false;
        bool m_negedge = false;
        bool m_changed = false;
    };
} // namespace dspedal
