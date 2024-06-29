include_guard(GLOBAL)

if (NOT TARGET Python::Module)
  message(FATAL_ERROR "You must invoke 'find_package(Python COMPONENTS Interpreter Development REQUIRED)' prior to including dspedal.")
endif()

# Set project paths.
cmake_path(GET dspedal_DIR PARENT_PATH DSPEDAL_DIR)

set(DSPEDAL_HDL_DIR ${DSPEDAL_DIR}/hdl)
set(DSPEDAL_INCLUDE_DIR ${DSPEDAL_DIR}/include)
set(DSPEDAL_GEN_DIR ${DSPEDAL_DIR}/Generated)

# Create verilated models
function(dspedal_add_model)
    set(options TRACE_FST)
    set(oneValueArgs HDL_SOURCE)
    set(multiValueArgs VERILATOR_ARGS INCLUDE_DIRS)
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(ARG_TARGET ${ARG_UNPARSED_ARGUMENTS})

    get_filename_component(MODULE_NAME ${ARG_HDL_SOURCE} NAME_WLE)

    # Trace type
    if(${ARG_TRACE_FST})
        set(TRACE_TYPE TRACE_FST)
        set(TRACE_CLI_ARG "--trace-fst")
    else()
        set(TRACE_TYPE TRACE)
        set(TRACE_CLI_ARG "")
    endif()

    # Generating modules
    # Find generate script
    if (EXISTS ${DSPEDAL_DIR}/src/dspedal/generate.py)
        set(DSPEDAL_GENERATE "${DSPEDAL_DIR}/src/dspedal/generate.py")
    elseif (EXISTS ${DSPEDAL_DIR}/generate.py)
        set(DSPEDAL_GENERATE "${DSPEDAL_DIR}/generate.py")
    else()
        message(FATAL_ERROR "Could not locate 'dspedal/stubgen.py'!")
    endif()
    message("DSPEDAL Generate: ${DSPEDAL_GENERATE}")

    list(APPEND GENERATE_ARGS ${ARG_HDL_SOURCE})
    list(APPEND GENERATE_ARGS -output_directory ${DSPEDAL_GEN_DIR})
    list(APPEND GENERATE_ARGS -include_dirs ${ARG_INCLUDE_DIRS})
    list(APPEND GENERATE_ARGS ${TRACE_CLI_ARG})
    list(APPEND GENERATE_ARGS ${ARG_VERILATOR_ARGS})

    set(GENERATE_CMD "${Python_EXECUTABLE}" "${DSPEDAL_GENERATE}" ${GENERATE_ARGS})
    # Run generate script.
    add_custom_command(
        OUTPUT ${DSPEDAL_GEN_DIR}/${MODULE_NAME}.h
        COMMAND ${GENERATE_CMD}
        COMMENT "Generate Python models"
    )
    add_custom_target(${ARG_TARGET}_generate DEPENDS
        ${DSPEDAL_GEN_DIR}/${MODULE_NAME}.h
    )

    # add_library(${ARG_TARGET} ${DSPEDAL_GEN_DIR}/${MODULE_NAME}.h)
    target_include_directories(${ARG_TARGET} PRIVATE ${DSPEDAL_GEN_DIR} ${DSPEDAL_INCLUDE_DIR})
    add_dependencies(${ARG_TARGET} ${ARG_TARGET}_generate)
    
    verilate(${ARG_TARGET} ${TRACE_TYPE}
        SOURCES ${ARG_HDL_SOURCE}
        INCLUDE_DIRS ${DSPEDAL_INCLUDE_DIR}
        VERILATOR_ARGS ${ARG_VERILATOR_ARGS}
    )
endfunction()
