# # Build base library
# dspedal_build_library(dspedal)
add_library(dspedal INTERFACE)
target_include_directories(dspedal INTERFACE ${DSPEDAL_INCLUDE_DIR})

# Framework module
nanobind_add_module(_framework NB_DOMAIN dspedal STABLE_ABI NB_STATIC _framework.cpp)
# target_include_directories(_framework PRIVATE ${DSPEDAL_INCLUDE_DIR})
target_link_libraries(_framework PRIVATE dspedal)

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
target_link_libraries(_library PRIVATE dspedal)
target_include_directories(_library PRIVATE ${DSPEDAL_GEN_DIR})

# Bind models and link to library
dspedal_add_model(_library
  TRACE_FST
  HDL_SOURCE ${DSPEDAL_HDL_DIR}/Skid.sv
  INCLUDE_DIRS ${DSPEDAL_HDL_DIR}
)

# Verilate it
# verilate(_library TRACE
#     SOURCES ${DSPEDAL_HDL_DIR}/Skid.sv
#     INCLUDE_DIRS ${DSPEDAL_HDL_DIR}
# )
install(TARGETS _library LIBRARY DESTINATION dspedal)
