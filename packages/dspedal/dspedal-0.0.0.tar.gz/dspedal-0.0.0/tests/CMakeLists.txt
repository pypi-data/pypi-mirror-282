include(CTest)
include(Catch)

# Run all tests target. Tests are excluded from "all" builds.
add_custom_target(run_all_tests)

# Create a test executable with provided sources, link to catch, and add as a dependency to run_all_tests
macro(create_test)
    set(options OPTIONAL)
    set(oneValueArgs EXTRA)
    set(multiValueArgs SOURCES)
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(ARG_TARGET ${ARG_UNPARSED_ARGUMENTS})

    add_executable(${ARG_TARGET} ${ARG_SOURCES})
    target_link_libraries(${ARG_TARGET} PRIVATE Catch2::Catch2WithMain)
    target_include_directories(test_context PRIVATE ${DSPEDAL_INCLUDE_DIR})

    catch_discover_tests(${ARG_TARGET})
    add_dependencies(run_all_tests ${ARG_TARGET})
endmacro()

create_test(test_context SOURCES test_context.cpp)
# target_link_libraries(test_context PRIVATE dspedal)

verilate(test_context TRACE_FST
    SOURCES ${DSPEDAL_HDL_DIR}/Skid.sv
    INCLUDE_DIRS ${DSPEDAL_HDL_DIR}
    OPT_GLOBAL
    VERILATOR_ARGS --quiet
)
