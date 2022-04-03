# CMakeLists.txt

# Set the minimum version of CMake that can be used
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# Set the C++ version
set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_POSITION_INDEPENDENT_CODE ON)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -O3 -g")

# Set the project name 
project(kuramoto_cpp)

# Project directories
set(SRC_DIR "cpp/src")

# Check whether this project is being built with cikit-build 
if(SKBUILD)
	message(STATUS "The project is built using scikit-build")
	# Scikit-Build does not add your site-packages to the search path
	# automatically, so we need to add it _or_ the pybind11 specific directory
	# here.
	execute_process(
	COMMAND "${PYTHON_EXECUTABLE}" -c
	        "import pybind11; print(pybind11.get_cmake_dir())"
	OUTPUT_VARIABLE _tmp_dir
	OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
	list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

# Include your .cpp sources here
set(SOURCE_FILES 
	${SRC_DIR}/pybind.cpp
	${SRC_DIR}/operators.cpp
)

# Use PyBind11
find_package(pybind11 CONFIG REQUIRED)

# Add C++ extensions
pybind11_add_module(kuramoto_cpp MODULE ${SOURCE_FILES})

# Link & install
target_link_libraries(kuramoto_cpp PRIVATE)
target_compile_definitions(kuramoto_cpp PUBLIC)
install(TARGETS kuramoto_cpp LIBRARY DESTINATION .)
