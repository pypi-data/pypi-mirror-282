cmake_minimum_required(VERSION 3.27)
project(dspedal LANGUAGES CXX)

if (CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
  set(DSPEDAL_MASTER_PROJECT ON)
  message("DSPedal Master Project.")
else()
  set(DSPEDAL_MASTER_PROJECT OFF)
endif()

option(DSPEDAL_TEST "Build tests." ${DSPEDAL_MASTER_PROJECT})

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_POSITION_INDEPENDENT_CODE On)

# Default build type.
if (DSPEDAL_MASTER_PROJECT AND NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Skip if building from another project.
if (DSPEDAL_MASTER_PROJECT AND NOT DSPEDAL_TEST)
  return()
endif()

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module Development.SABIModule)

find_package(nanobind CONFIG REQUIRED)
find_package(verilator CONFIG REQUIRED)
find_package(Catch2 3 REQUIRED)

# dspedal cmake config.
find_package(dspedal PATHS ${CMAKE_CURRENT_SOURCE_DIR}/src/dspedal/cmake NO_DEFAULT_PATH)

message("HDL_DIR: ${DSPEDAL_HDL_DIR}")
message("Include Dir: ${DSPEDAL_INCLUDE_DIR}")

add_subdirectory(src)

# Tests
if (DSPEDAL_TEST)
  enable_testing()
  add_subdirectory(tests)
endif()
