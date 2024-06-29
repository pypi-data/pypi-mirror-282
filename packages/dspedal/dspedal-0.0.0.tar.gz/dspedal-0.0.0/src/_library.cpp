#include "dspedal/dspedal.h"
#include "dspedal/bindings.h"

#include <nanobind/nanobind.h>
#include <nanobind/trampoline.h>
#include <nanobind/stl/shared_ptr.h>

#include <iostream>

// Models
#include "Skid.h"

using namespace dspedal;
namespace nb = nanobind;

class SomeModel : public Model
{
public:
    SomeModel()
    {
        std::cout << "Some Model ctor" << std::endl;
    }

    void eval_step()
    {
        std::cout << "Some Model eval_step" << std::endl;
    }

    void eval_end_step()
    {
        std::cout << "Some Model eval_end_step" << std::endl;
    }
};

NB_MODULE(_library, m)
{
    // Functions to get/set the module context.
    bind_module_context(m);

    // Bind a model.
    bind_model<SomeModel>(m, "SomeModel")
        .def(nb::init<>());

    create_Skid(m, "Skid");
    // bind_model<Skid>(m, "Skid")
    //     .def(nb::init<>());
}
