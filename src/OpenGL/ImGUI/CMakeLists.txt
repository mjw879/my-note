cmake_minimum_required(VERSION 3.15)
project(ImGUI)

include_directories(${CMAKE_SOURCE_DIR}/include)
add_compile_options(-std=c++11 -Wall -g )


add_subdirectory(${CMAKE_SOURCE_DIR}/chapter/1.example)
add_subdirectory(${CMAKE_SOURCE_DIR}/chapter/2.helloworld)