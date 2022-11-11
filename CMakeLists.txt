cmake_minimum_required( VERSION 3.15)
set(CMAKE_CXX_FLAGS "-std=c++11")
project(video)

find_package(OpenCV REQUIRED)
find_package(fmt REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(${fmt_INCLUDE_DIRS})

add_executable(video src/video.cpp)
target_link_libraries(video ${OpenCV_LIBRARIES})
target_link_libraries(video ${fmt_LIBRARIES})