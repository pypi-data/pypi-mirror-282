"""Generated library interface file."""

import dspedal.framework

def get_context() -> dspedal.framework.Context: ...
def set_context(context: dspedal.framework.Context) -> None: ...

class SomeModel:
    def __init__(self) -> None: ...
    @property
    def context(self) -> dspedal.framework.Context: ...
    def eval_step(self) -> None: ...
    def eval_end_step(self) -> None: ...

class Skid:
    def __init__(
        self,
        clk: dspedal.framework.Signal8,
        rst: dspedal.framework.Signal8,
        s_axis_tdata: dspedal.framework.Signal32,
        s_axis_tvalid: dspedal.framework.Signal8,
        s_axis_tready: dspedal.framework.Signal8,
        m_axis_tdata: dspedal.framework.Signal32,
        m_axis_tvalid: dspedal.framework.Signal8,
        m_axis_tready: dspedal.framework.Signal8,
    ) -> None: ...
    def trace(self, trace_name: str, levels: int = 99) -> None: ...
