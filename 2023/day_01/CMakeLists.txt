cmake_minimum_required(VERSION 3.24)
project(day_01 CXX)

file(GLOB_RECURSE SOURCE_FILES DEPENDS "*.cpp")
file(GLOB_RECURSE HEADER_FILES DEPENDS "*.h")

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE ${SOURCE_FILES} ${HEADER_FILES})
target_link_libraries(${PROJECT_NAME}
    PRIVATE
    aoc
)
