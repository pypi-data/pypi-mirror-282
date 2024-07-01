include_guard(GLOBAL)

if (NOT TARGET Python::Module)
  message(FATAL_ERROR "You must invoke 'find_package(Python COMPONENTS Interpreter Development REQUIRED)' prior to including dspedal.")
endif()

# Set project paths.
cmake_path(GET dspedal_DIR PARENT_PATH DSPEDAL_DIR)

set(DSPEDAL_HDL_DIR ${DSPEDAL_DIR}/hdl)
set(DSPEDAL_INCLUDE_DIR ${DSPEDAL_DIR}/include)

# Create verilated models
function(dspedal_add_model)
    set(oneValueArgs HDL_SOURCE GEN_DIR)
    set(multiValueArgs VERILATOR_ARGS INCLUDE_DIRS)
    cmake_parse_arguments(ARG "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    set(ARG_TARGET ${ARG_UNPARSED_ARGUMENTS})

    get_filename_component(MODULE_NAME ${ARG_HDL_SOURCE} NAME_WLE)

    # Generating modules
    # Find generate script
    if (EXISTS ${DSPEDAL_DIR}/src/dspedal/generate.py)
        set(DSPEDAL_GENERATE "${DSPEDAL_DIR}/src/dspedal/generate.py")
    elseif (EXISTS ${DSPEDAL_DIR}/generate.py)
        set(DSPEDAL_GENERATE "${DSPEDAL_DIR}/generate.py")
    else()
        message(FATAL_ERROR "Could not locate 'dspedal/stubgen.py'!")
    endif()

    list(APPEND GENERATE_ARGS ${ARG_HDL_SOURCE})
    list(APPEND GENERATE_ARGS -output_directory ${ARG_GEN_DIR})
    list(APPEND GENERATE_ARGS -include_dirs ${ARG_INCLUDE_DIRS} ${DSPEDAL_HDL_DIR})
    list(APPEND GENERATE_ARGS ${ARG_VERILATOR_ARGS})

    set(GENERATE_CMD "${Python_EXECUTABLE}" "${DSPEDAL_GENERATE}" ${GENERATE_ARGS})
    # Run generate script.
    add_custom_command(
        OUTPUT ${ARG_GEN_DIR}/${MODULE_NAME}.h
        COMMAND ${GENERATE_CMD}
        COMMENT "Generate Python models"
    )
    add_custom_target(${MODULE_NAME}_generate DEPENDS
        ${ARG_GEN_DIR}/${MODULE_NAME}.h
    )

    target_include_directories(${ARG_TARGET} PRIVATE ${ARG_GEN_DIR} ${DSPEDAL_INCLUDE_DIR})
    add_dependencies(${ARG_TARGET} ${MODULE_NAME}_generate)
    
    verilate(${ARG_TARGET} TRACE
        SOURCES ${ARG_HDL_SOURCE}
        INCLUDE_DIRS ${ARG_INCLUDE_DIRS} ${DSPEDAL_HDL_DIR}
        VERILATOR_ARGS ${ARG_VERILATOR_ARGS}
    )
endfunction()
