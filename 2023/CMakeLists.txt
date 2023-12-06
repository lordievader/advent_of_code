cmake_minimum_required(VERSION 3.24)

# Use clang
set(CMAKE_C_COMPILER "clang")
set(CMAKE_CXX_COMPILER "clang++")

# set the project name and version
project(aoc VERSION 2023.0.0)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_CLANG_TIDY clang-tidy)

set(CMAKE_CXX_FLAGS_DEBUG_INIT "-Wall")
set(CMAKE_CXX_FLAGS_RELEASE_INIT "-Wall")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_subdirectory(lib)
add_subdirectory(day_01)
add_subdirectory(day_02)
