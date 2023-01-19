cmake_minimum_required(VERSION 3.15)
project(ImGUI)

include_directories(${PROJECT_SOURCE_DIR}/include)

aux_source_directory(${PROJECT_SOURCE_DIR}/source source_dir)
add_compile_options(-std=c++11 -Wall -g )

if (${CMAKE_HOST_SYSTEM_NAME} MATCHES Linux)
    find_library(glfw3 libglfw3.a)
    find_library(GL libGL.so)
    find_library(X11 libX11.so)
    find_library(pthread libpthread.so)
    find_library(dl libdl.so)
elseif()
endif()



add_executable(${PROJECT_NAME} ${PROJECT_SOURCE_DIR}/main.cpp ${source_dir})
    
target_link_libraries(${PROJECT_NAME} ${glfw3})
target_link_libraries(${PROJECT_NAME} ${GL}) 
target_link_libraries(${PROJECT_NAME} ${X11}) 
target_link_libraries(${PROJECT_NAME} ${pthread}) 
target_link_libraries(${PROJECT_NAME} ${dl}) 