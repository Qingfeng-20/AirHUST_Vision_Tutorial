cmake_minimum_required(VERSION 3.12)
project(lab1_1)

find_package(OpenCV REQUIRED) 

set(SOURCES
    src/main.cpp
    src/image_io.cpp)
aux_source_directory(src sc_executable_source)
add_executable(${sc_executable_name} ${sc_executable_source})
target_include_directories(${sc_executable_name} BEFORE PUBLIC include)
target_link_libraries(${sc_executable_name}  ${OpenCV_LIBS})

