cmake_minimum_required(VERSION 3.15)

project(Demo)

message(${CMAKE_HOST_SYSTEM_NAME})

if (${CMAKE_HOST_SYSTEM_NAME} MATCHES Linux)
    message("hello")
endif()