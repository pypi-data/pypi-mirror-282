#pragma once

#include "dspedal/signal.h"
#include <deque>
#include <vector>
#include <initializer_list>

namespace dspedal
{
    // C
    template <typename T>
    struct Axis
    {
        Signal<T> tdata;
        Signal<uint8_t> tvalid;
        Signal<uint8_t> tready;
    };

    // Axis Master
    template <typename T>
    class AxisTx : public Model
    {
    public:
        Signal<uint8_t> &clk;
        Signal<uint8_t> &rst;
        Signal<T> &m_axis_tdata;
        Signal<uint8_t> &m_axis_tvalid;
        Signal<uint8_t> &m_axis_tready;

        AxisTx(Signal<uint8_t> &clk, Signal<uint8_t> &rst, Signal<T> &m_axis_tdata, Signal<uint8_t> &m_axis_tvalid, Signal<uint8_t> &m_axis_tready)
            : Model(), clk(clk), rst(rst),
              m_axis_tdata(m_axis_tdata), m_axis_tvalid(m_axis_tvalid), m_axis_tready(m_axis_tready)
        {
        }

        AxisTx(Signal<uint8_t> &clk, Signal<uint8_t> &rst, Axis<T> &m_axis)
            : AxisTx<T>(clk, rst, m_axis.tdata, m_axis.tvalid, m_axis.tready)
        {
        }

        virtual void eval_step()
        {
            if (clk.posedge())
            {
                // Output transaction accepted.
                if (m_axis_tvalid && m_axis_tready)
                {
                    m_axis_tvalid = 0;
                }

                // Data is available and the output is not stalled.
                if (!tx_buffer.empty() && (!m_axis_tvalid || m_axis_tready))
                {
                    m_axis_tdata = tx_buffer.front();
                    m_axis_tvalid = 1;
                    tx_buffer.pop_front();
                }

                if (rst)
                {
                    m_axis_tdata = 0;
                    m_axis_tvalid = 0;
                }
            }
        }

        void write(const T &x)
        {
            tx_buffer.push_back(x);
        }

        void write(const std::vector<T> &v)
        {
            tx_buffer.insert(tx_buffer.end(), v.begin(), v.end());
        }
        void write(const std::initializer_list<T> &v)
        {
            tx_buffer.insert(tx_buffer.end(), v.begin(), v.end());
        }
        // template <typename Iter>
        // void write(Iter begin, Iter end)
        // {
        //     tx_buffer.insert(tx_buffer.end(), begin, end);
        // }

    protected:
        std::deque<T> tx_buffer;
    };

    template <typename T>
    class AxisRx : public Model
    {
    public:
        Signal<uint8_t> &clk;
        Signal<uint8_t> &rst;
        Signal<T> &s_axis_tdata;
        Signal<uint8_t> &s_axis_tvalid;
        Signal<uint8_t> &s_axis_tready;

        AxisRx(Signal<uint8_t> &clk, Signal<uint8_t> &rst, Signal<T> &s_axis_tdata, Signal<uint8_t> &s_axis_tvalid, Signal<uint8_t> &s_axis_tready)
            : Model(), clk(clk), rst(rst),
              s_axis_tdata(s_axis_tdata), s_axis_tvalid(s_axis_tvalid), s_axis_tready(s_axis_tready)
        {
            next_tready = 0;
        }

        AxisRx(Signal<uint8_t> &clk, Signal<uint8_t> &rst, Axis<T> &s_axis)
            : AxisRx<T>(clk, rst, s_axis.tdata, s_axis.tvalid, s_axis.tready)
        {
        }

        void tready(uint8_t val)
        {
            next_tready = val;
        }
        const uint8_t tready(void) const
        {
            return s_axis_tready;
        }

        void set_tready(uint8_t value)
        {
            tready(value);
        }

        const uint8_t get_tready(void) const
        {
            return tready();
        }

        std::vector<T> read(void)
        {
            std::vector<T> result(rx_buffer.begin(), rx_buffer.end());
            rx_buffer.clear();
            return result;
        }

        T *read_new(void)
        {
            T *result = new T[rx_buffer.size()];
            size_t i = 0;
            for (const auto &x : rx_buffer)
            {
                result[i++] = x;
            }
            rx_buffer.clear();

            return result;
        }

        size_t size()
        {
            return rx_buffer.size();
        }

        void eval_step()
        {
            if (clk.posedge())
            {
                s_axis_tready = next_tready;

                // Previous transaction accepted.
                if (s_axis_tvalid && s_axis_tready)
                {
                    rx_buffer.push_back(s_axis_tdata);
                }

                if (rst)
                {
                }
            }
        }

    protected:
        std::deque<T> rx_buffer;
        uint8_t next_tready;
    };
} // namespace dspedal
