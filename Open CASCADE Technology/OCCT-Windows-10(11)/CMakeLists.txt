cmake_minimum_required (VERSION 3.9)

set(CMAKE_CONFIGURATION_TYPES "Debug;Release" CACHE STRING "Configurations" FORCE)

# Project name
project (HelloOpenCASCADE CXX)

### Configure output locations
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
 
# C++ standard 17.
# in C++17 the standard allocators have been updated to respect type's alignment.
set(CMAKE_CXX_STANDARD 17)

#find opencascade
find_package(OpenCASCADE)
include_directories(${OpenCASCADE_INCLUDE_DIR})
get_filename_component(PARENT_DIR ${OpenCASCADE_INSTALL_PREFIX} PATH)

#set opencascade
set(3RDPARTY_DIR ${PARENT_DIR}/products)  ## where products is the user-defined folder name for third-party libraries
set (OpenCASCADE_WITH_TCL       ON)
set (OpenCASCADE_WITH_FREETYPE  ON)
set (OpenCASCADE_WITH_FREEIMAGE OFF)
set (OpenCASCADE_WITH_TBB       OFF)
set (OpenCASCADE_WITH_VTK       OFF)
set (OpenCASCADE_WITH_FFMPEG    OFF)
set (OpenCASCADE_WITH_GLES2     OFF)
set (OpenCASCADE_WITH_D3D       OFF)

# add the header files and cpp files 
file(
    GLOB src_files
    src/*.cpp 
    src/*.h
)

INCLUDE_DIRECTORIES(src)

# Add executable
add_executable(HelloOpenCASCADE ${src_files})

# Add linker options
foreach (LIB ${OpenCASCADE_LIBRARIES})
  target_link_libraries(HelloOpenCASCADE debug ${OpenCASCADE_LIBRARY_DIR}/${LIB}.lib)
  target_link_libraries(HelloOpenCASCADE optimized ${OpenCASCADE_LIBRARY_DIR}/${LIB}.lib)
endforeach()

# Output
set_target_properties(HelloOpenCASCADE PROPERTIES LINK_FLAGS "/SUBSYSTEM:WINDOWS /ENTRY:mainCRTStartup /OUT:\"$(OutDir)$(TargetName)$(TargetExt)\"")
# Adjust runtime environment
message(${OpenCASCADE_BINARY_DIR})
set_property(TARGET HelloOpenCASCADE PROPERTY VS_DEBUGGER_ENVIRONMENT "PATH=$<$<CONFIG:DEBUG>:${OpenCASCADE_BINARY_DIR}d>$<$<NOT:$<CONFIG:DEBUG>>:${OpenCASCADE_BINARY_DIR}>;%PATH%")

Add_Definitions(-DUNICODE)