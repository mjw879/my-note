cmake_minimum_required(VERSION 3.15)

project(Demo5)

set (EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

add_compile_options(-std=c++11 -Wall)

add_executable(main ${PROJECT_SOURCE_DIR}/main.cpp)