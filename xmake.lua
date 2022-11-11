add_requires("opencv", "fmt", "ffmpeg")

target("video")
    set_kind("binary")
    set_languages("c++20")
    add_files("src/*.cpp")
    add_packages("opencv", "fmt", "ffmpeg")