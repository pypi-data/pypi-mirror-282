#pragma once
#include "dspedal/dspedal.h"

#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/trampoline.h>
#include <nanobind/ndarray.h>

NB_MAKE_OPAQUE(dspedal::Context);
NB_MAKE_OPAQUE(dspedal::Model);
NB_MAKE_OPAQUE(dspedal::Signal<uint8_t>);
NB_MAKE_OPAQUE(dspedal::Signal<uint16_t>);
NB_MAKE_OPAQUE(dspedal::Signal<uint32_t>);

namespace dspedal
{
    // Allows inheriting Model with a Python class.
    struct PyModel : public Model
    {
        NB_TRAMPOLINE(Model, 2);

        void eval_step() override
        {
            NB_OVERRIDE_PURE(eval_step);
        }
        void eval_end_step() override
        {
            NB_OVERRIDE(eval_end_step);
        }
    };

    // Module level get/set context.
    static inline auto bind_module_context(nanobind::module_ &m)
    {
        return m.def("get_context", []()
                     { return Model::context(); }, nanobind::rv_policy::reference, nanobind::sig("def get_context() -> dspedal.framework.Context"))
            .def("set_context", [](ContextPtr context)
                 { Model::context(context); }, nanobind::sig("def set_context(context: dspedal.framework.Context) -> None"));
    }

    // Bind context.
    static inline auto bind_context(nanobind::handle &scope, const char *name)
    {
        return // Context
            nanobind::class_<Context>(scope, name)
                .def(nanobind::init<>())
                .def("clear", &Context::clear)
                .def("register_model", &Context::register_model, nanobind::arg("model"))
                .def("time_inc", &Context::time_inc, nanobind::arg("time_step"))
                .def("time", &Context::time);
    }

    // Bind Model.
    static inline auto bind_base_model(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Model, PyModel>(scope, name)
            .def(nanobind::init<>())
            .def_prop_ro("context", &Model::get_context)
            .def("eval_step", &Model::eval_step)
            .def("eval_end_step", &Model::eval_end_step);
    }

    // Bind a custom model.
    template <typename M>
    static inline auto bind_model(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<M, Model>(scope, name)
            .def_prop_ro("context", &M::get_context, nanobind::sig("def context(self) -> dspedal.framework.Context"))
            .def("eval_step", &M::eval_step)
            .def("eval_end_step", &M::eval_end_step);
    }

    // Simulator
    static inline auto bind_simulator(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Simulator>(scope, name)
            .def(nanobind::init<>())
            .def("eval", &Simulator::eval)
            .def("advance", &Simulator::advance, nanobind::arg("time_inc"))
            .def("reset", &Simulator::reset, nanobind::arg("rst"), nanobind::arg("duration") = 100);
    }

    // Templates to make all signal and DFF types.
    template <typename T>
    static inline auto bind_signal(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Signal<T>>(scope, name)
            // Default constructor
            .def(nanobind::init<T>(),
                 nanobind::arg("initial") = 0)

            .def("posedge", &Signal<T>::posedge)
            .def("negedge", &Signal<T>::negedge)
            .def("changed", &Signal<T>::changed)
            .def_prop_rw(
                "d", [](Signal<T> *s)
                { return s->_read_d(); },
                [](Signal<T> *s, int val)
                { s->writei(val); })
            .def_prop_ro("q", &Signal<T>::read);
    }

    // Bind Clock.
    template <typename T = uint8_t>
    static inline auto bind_clock(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Clock<T>, Signal<T>>(scope, name)
            .def(nanobind::init<uint64_t>(), nanobind::arg("period"))
            .def_prop_ro("period", &Clock<uint8_t>::period);
    }

    // Templates to make all signal and DFF types.
    template <typename T>
    static inline auto bind_dff(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Dff<T>, Signal<T>>(scope, name)
            // Default constructor
            .def(nanobind::init<Signal<uint8_t> &, T>(),
                 nanobind::arg("clk"),
                 nanobind::arg("initial") = 0)

            .def_prop_rw(
                "d", [](Dff<T> *s)
                { return s->_read_d(); },
                [](Dff<T> *s, int val)
                { s->writei(val); })
            .def_prop_ro("q", &Dff<T>::read);
    }

    // AXIS templates
    template <typename T>
    static inline auto bind_axis(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<Axis<T>>(scope, name)
            .def(nanobind::init<>())
            .def_ro("tdata", &Axis<T>::tdata)
            .def_ro("tvalid", &Axis<T>::tvalid)
            .def_ro("tready", &Axis<T>::tready);
    }
    // AxisTx
    template <typename T>
    static inline auto bind_axis_tx(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<AxisTx<T>, Model>(scope, name)
            .def(nanobind::init<
                     Signal<uint8_t> &,
                     Signal<uint8_t> &,
                     Signal<T> &,
                     Signal<uint8_t> &,
                     Signal<uint8_t> &>(),
                 nanobind::arg("clk"),
                 nanobind::arg("rst"),
                 nanobind::arg("m_axis_tdata"),
                 nanobind::arg("m_axis_tvalid"),
                 nanobind::arg("m_axis_tready"))
            .def(nanobind::init<
                     Signal<uint8_t> &,
                     Signal<uint8_t> &,
                     Axis<T> &>(),
                 nanobind::arg("clk"),
                 nanobind::arg("rst"),
                 nanobind::arg("m_axis"))

            .def("write", nanobind::overload_cast<const T &>(&AxisTx<T>::write), nanobind::arg("value"))
            .def("write", nanobind::overload_cast<const std::vector<T> &>(&AxisTx<T>::write), nanobind::arg("tx_data"));
    }

    // AxisRx
    template <typename T>
    static inline auto bind_axis_rx(nanobind::handle &scope, const char *name)
    {
        return nanobind::class_<AxisRx<T>, Model>(scope, name)
            .def(nanobind::init<
                     Signal<uint8_t> &,
                     Signal<uint8_t> &,
                     Signal<T> &,
                     Signal<uint8_t> &,
                     Signal<uint8_t> &>(),
                 nanobind::arg("clk"),
                 nanobind::arg("rst"),
                 nanobind::arg("s_axis_tdata"),
                 nanobind::arg("s_axis_tvalid"),
                 nanobind::arg("s_axis_tready"))
            .def(nanobind::init<
                     Signal<uint8_t> &,
                     Signal<uint8_t> &,
                     Axis<T> &>(),
                 nanobind::arg("clk"),
                 nanobind::arg("rst"),
                 nanobind::arg("s_axis"))

            // .def("read", &AxisRx<T>::read)
            .def("size", &AxisRx<T>::size)
            .def("__len__", &AxisRx<T>::size)
            .def("read", [](AxisRx<T> &axis)
                 {
                    size_t xsize = axis.size();
                    T *v = axis.read_new();
                    nanobind::capsule deleter(v, [](void *p) noexcept
                        { delete[] (T *)p; });

                    return nanobind::ndarray<nanobind::numpy, T, nanobind::ndim<1>>(v, {xsize}, deleter); })
            .def_prop_rw("tready", &AxisRx<T>::get_tready, &AxisRx<T>::set_tready, nanobind::arg("value"));
    }

} // namespace dspedal
