# libHexEx 配置记录

本文档为配置文章 “HexEx: robust hexahedral mesh extraction” 的代码的记录 [[doi]](https://dl.acm.org/doi/abs/10.1145/2897824.2925976) [[project]](https://www.graphics.rwth-aachen.de/publication/03260/) [[software]](https://www.graphics.rwth-aachen.de/software/libHexEx/) [[code]](https://gitlab.vci.rwth-aachen.de:9000/HexEx/libHexEx)

```
@article{10.1145/2897824.2925976,
    author = {Lyon, Max and Bommes, David and Kobbelt, Leif},
    title = {HexEx: robust hexahedral mesh extraction},
    year = {2016},
    issue_date = {July 2016},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {35},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2897824.2925976},
    doi = {10.1145/2897824.2925976},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {123},
    numpages = {11},
    keywords = {hex meshing, mesh extraction, parametrization}
}
```

---

Canjia Huang <<canjia7@gmail.com>> update 27/6/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：
    ```
    git clone https://gitlab.vci.rwth-aachen.de:9000/HexEx/libHexEx.git
    ```

    进入项目目录：
    ```
    cd libHexEx
    ```

2. 新建存放编译结果的目录并进入：
    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure：
    ```
    cmake ..
    ```

    - :warning: 可能会出现与 **OpenVolumeMesh** 库相关的错误 `"OPENVOLUMEMESH_INCLUDE_DIR-NOTFOUND"` 等，虽然仍能生成 make 文件，但后续编译会出错
        需要配置 **OpenVolumeMesh** 库，具体步骤可以参考 [OpenVolumeMesh 配置记录](../OpenVolumeMesh/)
        为了方便，可以将 **OpenVolumeMesh** 库安装在 libHexEx 的根目录，该项目的 CMake 会自动识别该路径，否则需要额外设置 `OPENVOLUMEMESH_INCLUDE_DIR` 变量
        配置完成后移除 “build” 目录并重新进行 2-3 步

4. 编译：
    ```
    make -j
    ```

    - :warning: 可能出现错误 `‘optional’ in namespace ‘std’ does not name a template type`
        参考 [ [1] ]，该问题是由于 CMake 没有启用 C++17 导致的，在 “libHexEx/CMakeLists.txt” 的 Line 23 处添加 `add_compile_options(-std=c++17)`，然后重新使用 CMake 进行 configure 并编译
    
    - :warning: 可能出现错误 `error: binding reference of type ‘int&’ to ‘const int’ discards qualifiers`
        参考 [ [2] ]，将 “OpenVolumeMesh/src/OpenVolumeMesh/Core/Handles.hh” 文件的 Line 82 `constexpr int& idx_mutable() { return idx_; }` 去掉 `constexpr`，然后重新编译

    - :warning: 可能出现错误 `error: no match for ‘operator!=’ (operand types are ‘const int’ and ‘HexEx::CellHandle’ {aka ‘OpenVolumeMesh::CH’})`
        该语句只用于简单输出警告，简单的处理方法是将该语句注释掉，即对文件 “/home/huangcanjia/libHexEx/src/HexExtractor.cc” 的 Line 4442-4445 进行注释

## 测试

编译成功后，在目录 “libHexEx/build/demo” 中会有两个包含可执行文件的目录，进入其中的 “minimum_example”，执行可执行文件：
```
./minimum_example
```

[1]: https://blog.csdn.net/a19910423/article/details/122476029
[2]: https://blog.csdn.net/weixin_46028606/article/details/105748895