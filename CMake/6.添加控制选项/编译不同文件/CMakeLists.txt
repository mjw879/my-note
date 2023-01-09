cmake_minimum_required(VERSION 3.15)

project(Demo6_1)

option(IS_BUILD_MAIN1 "build main1.cpp or main2.cpp" OFF) # 命令行运行 `cmake .. -DIS_BUILD_MAIN1=ON` 来控制该option  

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

add_subdirectory(src)
