cmake_minimum_required(VERSION 3.15)

project(Demo4)

include_directories(${PROJECT_SOURCE_DIR}/include)

find_library(myLib libmyFunc.a HINTS ${PROJECT_SOURCE_DIR}/lib) # 在指定目录下查找指定库，并把库的绝对路径存放到变量里。第一个参数是变量名称，第二个参数是库名称，第三个参数是HINTS，第4个参数是路径

add_executable(main ${PROJECT_SOURCE_DIR}/main.cpp)

target_link_libraries(main ${myLib}) # 把目标文件与库文件进行链接