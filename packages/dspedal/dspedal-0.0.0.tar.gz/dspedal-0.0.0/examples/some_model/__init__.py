import dspedal.framework

from ._some_model import *

set_context(dspedal.framework.get_context())

__all__ = [
    "set_context",
    "get_context",
    "foo",
]
