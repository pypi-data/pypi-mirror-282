cmake_minimum_required(VERSION 3.27)
project(dspedal LANGUAGES CXX)

if (CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
  set(DSPEDAL_MASTER_PROJECT ON)
  message("DSPedal Master Project.")
else()
  set(DSPEDAL_MASTER_PROJECT OFF)
endif()

# option(DSPEDAL_TEST "Build tests." ${DSPEDAL_MASTER_PROJECT})
option(BUILD_TESTING "Build tests." On)
# set(CMAKE_CXX_STANDARD 20)
# set(CMAKE_POSITION_INDEPENDENT_CODE On)

# Default build type.
if (DSPEDAL_MASTER_PROJECT AND NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Skip if building from another project.
if (NOT DSPEDAL_MASTER_PROJECT AND NOT DSPEDAL_TEST)
  return()
endif()

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module Development.SABIModule)

find_package(nanobind CONFIG REQUIRED)
find_package(verilator CONFIG REQUIRED)
message("Found Verilator: ${verilator_DIR}")
# find_package(Catch2 3 REQUIRED)

# dspedal cmake config.
find_package(dspedal PATHS ${CMAKE_CURRENT_SOURCE_DIR}/src/dspedal/cmake NO_DEFAULT_PATH)

add_subdirectory(src)

# Tests
if (BUILD_TESTING)
  Include(FetchContent)

  FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG v3.6.0
  )

  FetchContent_MakeAvailable(Catch2)
  include(CTest)
  add_subdirectory(tests)
endif()
