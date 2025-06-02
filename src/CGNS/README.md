# CGNS 库配置记录

[CFD General Notation System (CGNS) 官网](https://cgns.github.io/index.html)

---

Canjia Huang <<canjia7@gmail.com>> last update 26/2/2025

# :apple: macOS

- 操作平台：MacBook Air (Apple M3) - macOS 15.3

## 安装步骤

详细且完整的步骤可以参考 [https://github.com/CGNS/CGNS](https://github.com/CGNS/CGNS) 的 README，以下为简单可行的安装步骤：

1. 首先安装 **HDF5**，推荐使用 **Homebrew** 安装，在终端中输入：
   
   ```
   brew install hdf5
   ```
   
   安装完成后可以在终端中使用指令 `brew list hdf5` 来查看 **HDF5** 的安装路径，我的位置为：/opt/homebrew/Cellar/hdf5/1.14.6 （:warning: 具体位置视具体情况，本文档以此为例）

2. 将 [CGNS](https://github.com/CGNS/CGNS) 库 clone 到本地，在终端中输入：
   
   ```
   git clone https://github.com/CGNS/CGNS.git
   ```

   本文档中我 clone 的路径为：/Users/canjia/CGNS，后续均以此路径为例（:warning: 具体路径因人而异，需作相应修改）

3. 在终端中进入 clone 的 **CGNS** 库路径，根据常规 **CMake** 项目操作进行 configuration：

    ```
    cd /Users/canjia/CGNS
    mkdir build
    cd build
    cmake .. -DCMAKE_PREFIX_PATH=******
    ```

    :warning: 注意，这里的 `cmake .. -DCMAKE_PREFIX_PATH=******` 中的星号需要替换为你的 **HDF5** 安装路径，例如我这里替换为 `cmake .. -DCMAKE_PREFIX_PATH=/opt/homebrew/Cellar/hdf5/1.14.6`

    然后继续在终端中进行编译安装：

    ```
    make -j
    make install
    ```

    :no_entry_sign: 执行 `make install` 时可能会报错 “file cannot create directory: /usr/local/lib.  Maybe need administrative
  privileges.”，改为执行 `sudo make install` 然后输入密码即可

## 在 CMake 项目中使用

需要在 **CMakeLists.txt** 中添加以下附加包含目录以及链接库：

```
find_package(CGNS REQUIRED)
include_directories("${CGNS_ROOT}/src")
include_directories("${CGNS_ROOT}/build/src")

...

target_link_libraries(${PROJECT_NAME} "${CGNS_ROOT}/build/src/libcgns.dylib")
```

:bulb: 这里的变量 **CGNS_ROOT** 并不是在系统环境变量中定义的，而是在 `find_package(CGNS)` 后由 **CGNS** 中的 config.cmake 来定义的，所以并不需要提前定义

## Some Resources

- [Some CGNS examples](https://cgns.github.io/current/examples.html)