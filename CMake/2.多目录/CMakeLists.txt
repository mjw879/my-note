cmake_minimum_required(VERSION 3.15)

PROJECT(Demo2)

include_directories(${CMAKE_SOURCE_DIR}/include)

aux_source_directory(${CMAKE_SOURCE_DIR}/source source_dir)

add_executable(${PROJECT_NAME} ${PROJECT_SOURCE_DIR}/main.cpp ${source_dir})
