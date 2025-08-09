## SuiteSparse Windows11配置

By Shi Chen 03/08/2025

[SuiteSparse](https://people.engr.tamu.edu/davis/suitesparse.html)是一个常见的稀疏矩阵计算库，本文为在Window11的配置流程。

### 一个好项目

- [suitesparse-metis-for-windows](https://github.com/jlblancoc/suitesparse-metis-for-windows)

我们基于这个指南来进行配置，下面这些步骤基本上就是把指南的流程走了一遍然后英译中放到这里，其实直接生吃这个指南也行，**指南也有针对`Linux/Mac`的内容**，本文只在Window11上使用Visual Studio进行配置。

### 前期准备

- 下载CMake，官网下载即可，我用的版本是3.29.7。
- 下载[Releases · jlblancoc/suitesparse-metis-for-windows](https://github.com/jlblancoc/suitesparse-metis-for-windows/releases)。
- 解压到本地目录，**假设这里放到的目录是`E:/Library/SR_ROOT/suitesparse-metis-for-windows`**。

### 配置过程

在仓库目录下使用cmake-gui：
1. Source code填：`E:/Library/SR_ROOT/suitesparse-metis-for-windows`。
2. Build directory填：`E:/Library/SR_ROOT/suitesparse-metis-for-windows/build`。
3. 点击“Configure”。
4. **仓库作者强调的内容**：`CMAKE_INSTALL_PREFIX`设置为`{Build directory}/install`，也就是你前面填的`build`目录下，**这里是作者的默认设置**，否则会安装到系统目录（需要管理员权限）。
5. 点击”Generate“。
6. Visual Studio打开项目，点击`INSTALL`项目**分别在Debug和Release模式下执行“生成”**。
7. 确认一下你的`insatll`目录下是否有`suitesparse-config.cmake`或`SuiteSparseConfig.cmake`文件，例如我的位置是在`.../build/install/lib/cmake/suitesparse-7.5.1`， 这是后续项目中`SuiteSparse_DIR `需要设置的地方。
8. 把`E:\Library\SR_ROOT\suitesparse-metis-for-windows\build\lib\Debug`和`E:\Library\SR_ROOT\suitesparse-metis-for-windows\build\lib\Release`,添加到`PATH`。

### 在你的项目中用上

以下是一个`CMakeLists.txt`配置的例子:

```

	cmake_minimum_required(VERSION 3.15)
	project(MyProject LANGUAGES CXX)
	
	set(CMAKE_CXX_STANDARD 14)
	
	# 指定 SuiteSparse 的路径
	set(SuiteSparse_ROOT_DIR "E:/Library/SR_ROOT/suitesparse-metis-for-windows/build/install")
	set(SuiteSparse_INCLUDE_DIR "${SuiteSparse_ROOT_DIR}/include/suitesparse")
	set(SuiteSparse_DIR "${SuiteSparse_ROOT_DIR}/lib/cmake/suitesparse-7.5.1")
	
	# 查找 SuiteSparse
	find_package(SuiteSparse CONFIG REQUIRED)
	
	add_executable(MyProject main.cpp)
	
	# 包含头文件
	target_include_directories(MyProject PUBLIC 
		${SuiteSparse_INCLUDE_DIR}
	)
	# 链接需要的库
	target_link_libraries(MyProject PRIVATE
	    SuiteSparse::cholmod
	)

```