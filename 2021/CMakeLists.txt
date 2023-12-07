cmake_minimum_required(VERSION 3.10)

# Use clang
#set(CMAKE_C_COMPILER "clang")
#set(CMAKE_CXX_COMPILER "clang++")

# set the project name and version
project(aoc VERSION 2021.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_CXX_FLAGS_DEBUG_INIT "-Wall")
set(CMAKE_CXX_FLAGS_RELEASE_INIT "-Wall")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(day_01 lib/functions.cpp day_01/main.cpp)
add_executable(day_02 lib/functions.cpp day_02/main.cpp)
add_executable(day_03 lib/functions.cpp day_03/main.cpp)
add_executable(day_04 lib/functions.cpp day_04/main.cpp)
