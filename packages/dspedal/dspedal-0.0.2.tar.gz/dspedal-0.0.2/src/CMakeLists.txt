# # Build base library
# dspedal_build_library(dspedal)
set(GEN_DIR ${CMAKE_BINARY_DIR}/Generated)
message("GEN_DIR: ${GEN_DIR}")

# Framework module
nanobind_add_module(_framework NB_DOMAIN dspedal STABLE_ABI NB_STATIC _framework.cpp)
target_include_directories(_framework PRIVATE ${DSPEDAL_INCLUDE_DIR})

# Verilate so we can get link verilated and vcd/fst
verilate(_framework TRACE
  SOURCES ${DSPEDAL_HDL_DIR}/Skid.sv
  PREFIX VDummySkidVcd
)

nanobind_add_stub(
    _framework_stub
    INSTALL_TIME
    MODULE _framework
    OUTPUT dspedal/_framework.pyi
    PYTHON_PATH $<TARGET_FILE_DIR:_framework>
    DEPENDS _framework
    MARKER_FILE dspedal/py.typed
    )

install(TARGETS _framework LIBRARY DESTINATION dspedal)

# Library module
nanobind_add_module(_library NB_DOMAIN dspedal STABLE_ABI NB_STATIC _library.cpp)
target_include_directories(_library PRIVATE ${DSPEDAL_INCLUDE_DIR} ${GEN_DIR})

nanobind_add_stub(
  _library_stub
  INSTALL_TIME
  MODULE _library
  OUTPUT dspedal/_library.pyi
  PYTHON_PATH $<TARGET_FILE_DIR:_library>
  DEPENDS _library
#   MARKER_FILE pysim/py.typed
)

# Bind models and link to library
dspedal_add_model(_library
  HDL_SOURCE ${DSPEDAL_HDL_DIR}/Skid.sv
  GEN_DIR ${GEN_DIR}
)
dspedal_add_model(_library
  HDL_SOURCE ${DSPEDAL_HDL_DIR}/Gain.sv
  GEN_DIR ${GEN_DIR}
)
dspedal_add_model(_library
  HDL_SOURCE ${DSPEDAL_HDL_DIR}/IIR.sv
  GEN_DIR ${GEN_DIR}
)

install(TARGETS _library LIBRARY DESTINATION dspedal)
