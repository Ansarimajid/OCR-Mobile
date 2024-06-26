# For more information about using CMake with Android Studio, read the
# documentation: https://d.android.com/studio/projects/add-native-code.html

# Sets the minimum version of CMake required to build the native library.

cmake_minimum_required(VERSION 3.4.1)

# Creates and names a library, sets it as either STATIC or SHARED, and provides
# the relative paths to its source code. You can define multiple libraries, and
# CMake builds them for you. Gradle automatically packages shared libraries with
# your APK.
set(PaddleLite_DIR "D:/study/github/good/paddle/android")
#include_directories(${PaddleLite_DIR}/cxx/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

#include(D:/study/github/good/paddle/android/opencv4.1.0/arm64-v8a/cmake/OpenCVConfig.cmake)

set(OpenCV_DIR "D:/study/github/good/paddle/android/OpenCV-android-sdk/sdk/native/jni")
find_package(OpenCV REQUIRED)
message(STATUS "OpenCV libraries: ${OpenCV_LIBS}")
include_directories(${OpenCV_INCLUDE_DIRS})

set(CMAKE_CXX_FLAGS
    "${CMAKE_CXX_FLAGS} -ffast-math -Ofast -Os -DNDEBUG -fno-exceptions -fomit-frame-pointer -fno-asynchronous-unwind-tables -fno-unwind-tables"
)
set(CMAKE_CXX_FLAGS
    "${CMAKE_CXX_FLAGS} -fvisibility=hidden -fvisibility-inlines-hidden -fdata-sections -ffunction-sections -fexceptions"
)
set(CMAKE_SHARED_LINKER_FLAGS
    "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--gc-sections -Wl,-z,nocopyreloc")

add_library(
  # Sets the name of the library.
  Native
  # Sets the library as a shared library.
  SHARED
  # Provides a relative path to your source file(s).
  Native.cc pipeline.cc utils.cc cls_process.cc rec_process.cc det_process.cc db_post_process.cc clipper.cpp)

find_library(
  # Sets the name of the path variable.
  log-lib
  # Specifies the name of the NDK library that you want CMake to locate.
  log)

add_library(
  # Sets the name of the library.
  paddle_light_api_shared
  # Sets the library as a shared library.
  SHARED
  # Provides a relative path to your source file(s).
  IMPORTED)

set_target_properties(
  # Specifies the target library.
  paddle_light_api_shared
  # Specifies the parameter you want to define.
  PROPERTIES
    IMPORTED_LOCATION
    #${PaddleLite_DIR}/cxx/libs/${ANDROID_ABI}/libpaddle_light_api_shared.so
    ${CMAKE_CURRENT_SOURCE_DIR}/../jniLibs/${ANDROID_ABI}/libpaddle_light_api_shared.so
    # Provides the path to the library you want to import.
)

# Specifies libraries CMake should link to your target library. You can link
# multiple libraries, such as libraries you define in this build script,
# prebuilt third-party libraries, or system libraries.

target_link_libraries(
  # Specifies the target library.
  Native
  paddle_light_api_shared
  ${OpenCV_LIBS}
  GLESv2
  EGL
  jnigraphics
  ${log-lib})
