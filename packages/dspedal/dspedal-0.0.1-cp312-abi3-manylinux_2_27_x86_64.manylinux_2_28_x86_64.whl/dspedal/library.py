import dspedal.framework as _dspedal_framework

# Import the contents of the nanobind module.
from dspedal._library import *

# Set this module's context to the framework context when imported.
set_context(_dspedal_framework.get_context())
