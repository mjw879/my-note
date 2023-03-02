cmake_minimum_required(VERSION 3.15)

project(Demo6_2)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

#  通过命令行运行 cmake .. -DmyDefine1=ON -DmyDefine2=ON 来打开下面两个选项
option(myDefine1 "print myDefine1" OFF)
option(myDefine2 "print myDefine2" OFF)

if (myDefine1)
    add_compile_options(-DmyDefine1)
endif()

if (myDefine2)
    add_compile_options(-DmyDefine2)
endif()

add_executable(main ${PROJECT_SOURCE_DIR}/main.cpp)
