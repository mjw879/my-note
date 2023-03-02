cmake_minimum_required(VERSION 3.15)

project(Demo3)

set(SRC_LIST ${PROJECT_SOURCE_DIR}/myFunc/myFunc.cpp)

# 编译动态库
add_library(myFunc_shared SHARED ${SRC_LIST})
set_target_properties(myFunc_shared PROPERTIES OUTPUT_NAME "myFunc")

# 编译静态库
add_library(myFunc_static STATIC ${SRC_LIST})
set_target_properties(myFunc_static PROPERTIES OUTPUT_NAME "myFunc")

set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib) # 可选：设置产物库的输出路径


