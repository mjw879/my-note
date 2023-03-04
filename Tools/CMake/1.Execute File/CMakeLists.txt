cmake_minimum_required(VERSION 3.15)

project(Demo1)

add_executable(${PROJECT_NAME} ${PROJECT_SOURCE_DIR}/main.cpp)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin) # 可选：可执行文件输出路径