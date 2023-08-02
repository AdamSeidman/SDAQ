cmake_minimum_required(VERSION 3.13)
get_filename_component(buildDirRelFilePath "board"
    REALPATH BASE_DIR "${CMAKE_SOURCE_DIR}")
set(PICO_BOARD_HEADER_DIRS "${buildDirRelFilePath}")
set(PICO_BOARD "sdaq_strain_gauge2")

# initialize pico-sdk from GIT
# (note this can come from environment, CMake cache etc)
set(PICO_SDK_FETCH_FROM_GIT on)

# pico_sdk_import.cmake is a single file copied from this SDK
# note: this must happen before project()
include(cmake/pico_sdk_import.cmake)

project(my_project)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()
file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.cpp)

# rest of your project
include_directories(inc)
include_directories(src)
add_executable(pico_driver ${SOURCES})
target_link_libraries(pico_driver pico_stdlib hardware_i2c hardware_spi)
