cmake_minimum_required(VERSION 3.24)
project(aoc CXX)

file(GLOB_RECURSE SOURCE_FILES DEPENDS "*.cpp")
file(GLOB_RECURSE HEADER_FILES DEPENDS "*.h")

add_library(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${SOURCE_FILES} ${HEADER_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
