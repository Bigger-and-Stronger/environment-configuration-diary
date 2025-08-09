Isometric Injective Energies | Windows11配置


By Shi Chen 09/08/2025


#### 论文：

Du X, Kaufman D M, Zhou Q, et al. Isometric energies for recovering injectivity in constrained mapping[C]//SIGGRAPH Asia 2022 Conference Papers. 2022: 1-9.

[Paper]([duxingyi-charles.github.io/publication/isometric-energies-for-recovering-injectivity-in-constrained-mapping/Isometric-Energies-for-Recovering-Injectivity-in-Constrained-Mapping.pdf](https://duxingyi-charles.github.io/publication/isometric-energies-for-recovering-injectivity-in-constrained-mapping/Isometric-Energies-for-Recovering-Injectivity-in-Constrained-Mapping.pdf)) | [Code](https://github.com/duxingyi-charles/Isometric_Injective_Energies)

这篇工作干的事情是:
- 从你给的一个比较差(例如有翻转)的参数化出发，计算出一个(尽量)低畸变的单射，支持指定位置约束。

同时也含有作者另一篇论文(TLC)的方法：

Du X, Aigerman N, Zhou Q, et al. Lifting simplices to find injectivity[J]. ACM Trans. Graph., 2020, 39(4): 120.

[Paper](https://duxingyi-charles.github.io/publication/lifting-simplices-to-find-injectivity/Lifting-Simplices-to-Find-Injectivity.pdf) | [Code](https://github.com/duxingyi-charles/lifting_simplices_to_find_injectivity)


#### 依赖库

- Eigen3
- CLI11
- nlohmann_json
- nlopt
- ghc::filesystem
- suitesparse


#### 可能的问题


##### 网络问题

FetchContent下载时因为**网络问题**报错，可以自行配置依赖库(作者设置的FetchContent下载的库在Windows中`vcpkg`都可以配)，然后改一下`cmake`文件夹下的`.cmake`文件，例如`cli11.cmake`:

``` 

if(TARGET CLI11::CLI11)
    return()
endif()

find_package(cli11 CONFIG REQUIRED)
/*
include(FetchContent)
FetchContent_Declare(
    cli11
    GIT_REPOSITORY https://github.com/CLIUtils/CLI11.git
    GIT_TAG v1.9.0
)
FetchContent_MakeAvailable(cli11)
*/
```


其他的几个`.cmake`文件也是这样改。


##### SuiteSparse没找到

报错信息：

```

  Could not find a package configuration file provided by "SuiteSparse" with
  any of the following names:

    SuiteSparseConfig.cmake
    suitesparse-config.cmake

  Add the installation prefix of "SuiteSparse" to CMAKE_PREFIX_PATH or set
  "SuiteSparse_DIR" to a directory containing one of the above files.  If
  "SuiteSparse" provides a separate development package or SDK, be sure it
  has been installed.
Call Stack (most recent call first):
  CMakeLists.txt:60 (find_package)
```

我的suitesparse是参考下面这个项目配置的：
- [suitesparse-metis-for-windows](https://github.com/jlblancoc/suitesparse-metis-for-windows)

手动在`CMakeLists.txt`中设定路径，`# suitesparse`部分直接改成：
```
# suitesparse
set(SuiteSparse_ROOT_DIR "your/path/suitesparse-metis-for-windows/build/install")
set(SuiteSparse_INCLUDE_DIR "${SuiteSparse_ROOT_DIR}/include/suitesparse")
set(SuiteSparse_DIR "${SuiteSparse_ROOT_DIR}/lib/cmake/suitesparse-7.5.1")

find_package(SuiteSparse CONFIG REQUIRED)
target_include_directories(injectiveEnergy PUBLIC ${SuiteSparse_INCLUDE_DIR})
target_link_libraries(TLC_2D PRIVATE SuiteSparse::cholmod)
target_link_libraries(IsoTLC_2D PRIVATE SuiteSparse::cholmod)
target_link_libraries(solver_test PRIVATE SuiteSparse::cholmod)
target_link_libraries(distortion_2D PRIVATE SuiteSparse::cholmod)
target_link_libraries(distortion_3D PRIVATE SuiteSparse::cholmod)

```


##### The target was not found

```

CMake Error at CMakeLists.txt:32 (target_link_libraries):  
Target "solver_test" links to:  
  
nlopt::nlopt  
  
but the target was not found. Possible reasons include:  
  
* There is a typo in the target name.  
* A find_package call is missing for an IMPORTED target.  
* An ALIAS target is missing.  
  
  

CMake Error at CMakeLists.txt:36 (target_link_libraries):  
Target "TLC_2D" links to:  
  
nlopt::nlopt  
  
but the target was not found. Possible reasons include:  
  
* There is a typo in the target name.  
* A find_package call is missing for an IMPORTED target.  
* An ALIAS target is missing.  
  
  

CMake Error at CMakeLists.txt:40 (target_link_libraries):  
Target "IsoTLC_2D" links to:  
  
nlopt::nlopt  
  
but the target was not found. Possible reasons include:  
  
* There is a typo in the target name.  
* A find_package call is missing for an IMPORTED target.  
* An ALIAS target is missing.  
  
  

CMake Error at CMakeLists.txt:52 (target_link_libraries):  
Target "distortion_2D" links to:  
  
nlopt::nlopt  
  
but the target was not found. Possible reasons include:  
  
* There is a typo in the target name.  
* A find_package call is missing for an IMPORTED target.  
* An ALIAS target is missing.  
  
  

CMake Error at CMakeLists.txt:56 (target_link_libraries):  
Target "distortion_3D" links to:  
  
nlopt::nlopt  
  
but the target was not found. Possible reasons include:  
  
* There is a typo in the target name.  
* A find_package call is missing for an IMPORTED target.  
* An ALIAS target is missing.

```

我翻了一下`NLoptConfig.cmake`文件，好像就是大小写问题... ...

```

# Tell the user project where to find our headers and libraries

set (NLOPT_VERSION "2.7.1")

set (NLOPT_INCLUDE_DIRS "${CMAKE_CURRENT_LIST_DIR}/../../include")
set (NLOPT_LIBRARY_DIRS "${CMAKE_CURRENT_LIST_DIR}/../")

# Allows loading NLOPT settings from another project
set (NLOPT_CONFIG_FILE "${CMAKE_CURRENT_LIST_FILE}")

# List of compilation flags -DTOTO to export
set (NLOPT_DEFINITIONS "")

# Our library dependencies (contains definitions for IMPORTED targets)
include ("${CMAKE_CURRENT_LIST_DIR}/NLoptLibraryDepends.cmake")

# These are IMPORTED targets created by NLOPTLibraryDepends.cmake
set (NLOPT_LIBRARIES "NLopt::nlopt")


```


其他的库也可能报这种问题，按类似的步骤搜索一下自己对应的`.cmake`文件对齐一下名字即可。


#### 测试案例以及文件格式

生成完成后，在`...\build\Release`路径下， 使用作者提供的案例做个测试：

```

/* Mapping triangle mesh by optimizing TLC energy */

	./TLC_2D ../../examples/input.json 

/* Mapping triangle mesh by optimizing IsoTLC energy */

	./IsoTLC_2D ../../examples/input.json 


```

输入`.json`文件应该含有：
- 网格顶点信息: `restV`
- 网格顶点对应的初始参数化信息：`initV`
- 网格面片信息(存储顶点下标)： `F`
- 约束点信息：`handles`

示例：

```

{
    "restV": [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 1.0, 0.0]
    ],
    "initV": [
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0]
    ],
    "F": [
        [0, 1, 2],
        [0, 2, 3]
    ],
    "handles": [
        0,
        3
    ]
}

```


也就是说，**需要先做一个初始化的参数化**，这里可以简单使用**Tutte嵌入**来做。

例如你想做非凸边界约束的参数化，可以先用Tutte嵌入做个初始化，照理说这个初始化应该会很差很差，然后用这个工作来优化一下。