#include "dspedal/dspedal.h"
#include "dspedal/bindings.h"

// Models
#include "Skid.h"
#include "Gain.h"
#include "IIR.h"

double sc_time_stamp(void)
{
    return 0;
}

NB_MODULE(_library, m)
{
    // Functions to get/set the module context.
    dspedal::bind_module_context(m);

    // Bind models.
    Skid::create_binding(m, "Skid");
    Gain::create_binding(m, "Gain");
    IIR::create_binding(m, "IIR");
}
