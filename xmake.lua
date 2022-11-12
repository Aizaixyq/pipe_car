add_requires("fmt")
add_requires("opencv", {configs = {gtk = true}})

target("video")
    set_kind("binary")
    set_languages("c++20")
    add_files("src/*.cpp")
    add_packages("opencv", "fmt")