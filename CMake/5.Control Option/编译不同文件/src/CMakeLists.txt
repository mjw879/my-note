cmake_minimum_required(VERSION 3.15)

project(Demo6_1_1)

if (IS_BUILD_MAIN1)
    add_executable(main1 ${PROJECT_SOURCE_DIR}/main1.cpp)
    message(STATUS "build main1.cpp")
else()
    add_executable(main2 ${PROJECT_SOURCE_DIR}/main2.cpp)
    message(STATUS "build main2.cpp")
endif()

