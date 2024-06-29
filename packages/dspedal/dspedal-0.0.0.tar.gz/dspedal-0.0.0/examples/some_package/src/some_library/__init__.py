import dspedal.framework

# import dspedal._library
from ._some_library import *

# Set this module's context to the framework context when imported.
set_context(dspedal.framework.get_context())

# Make the model available.
__all__ = [
    "set_context",
    "get_context",
    "SomeModel",
]
