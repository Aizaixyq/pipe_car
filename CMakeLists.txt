cmake_minimum_required( VERSION 3.15)
set(CMAKE_CXX_FLAGS "-std=c++11")
project(video)

find_package(OpenCV REQUIRED)
message("opencv dir = ${OpenCV_INCLUDE_DIRS}")
message("Opencv lib = ${OpenCV_LIBRARIES}")
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(video src/video.cpp)
target_link_libraries(video ${OpenCV_LIBRARIES})