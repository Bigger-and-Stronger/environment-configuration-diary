# QuadWild with Bi-MDF solver 项目配置记录

本文档为配置文章 **"Min-Deviation-Flow in Bi-directed Graphs for T-Mesh Quantization"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/10.1145/3592437) [[Project Page]](https://www.algohex.eu/publications/bimdf-quantization/) [[Code]](https://github.com/cgg-bern/quadwild-bimdf)

```
@article{Heistermann:2023:BiMDF,
    author = {Heistermann, Martin and Warnett, Jethro and Bommes, David},
    title = {Min-Deviation-Flow in Bi-directed Graphs for T-Mesh Quantization},
    journal = {ACM Transactions on Graphics},
    volume = {42},
    number = {4},
    year = {2023},
    publisher = {ACM},
    address = {New York, NY, USA},
    doi = {10.1145/3592437}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 20/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置步骤

---

:star: 该项目有发布预先编译好的可执行文件，可直接在 [quadwild-bimdf/releases](https://github.com/cgg-bern/quadwild-bimdf/releases) 下载使用，不需要进行以下配置步骤

但使用该可执行文件似乎需要 root 权限 :open_mouth:，没有权限的话可能还是得进行编译

---

参考 [quadwild-bimdf/READMD](https://github.com/cgg-bern/quadwild-bimdf/blob/main/README.md)

1. 将项目下载到本地，在终端中输入：

    ```
    git clone --recursive https://github.com/cgg-bern/quadwild-bimdf/
    ```

    并进入该项目目录：

    ```
    cd quadwild-bimdf
    ```

2. 使用 CMake 进行 configure 和编译，在终端中执行：

    ```
    cmake . -B build -DSATSUMA_ENABLE_BLOSSOM5=0
    ```

    ```
    cmake --build build
    ```

    - :warning: 可能出现错误 `fatal error: span: No such file or directory`

        `span` 是一个 C++20 的标准头文件，该问题可能是 gcc 的版本太低导致的，可以参考 [ [1] ] 安装更新版本的 gcc（经测试，gcc 10.1 版本可以编译成功）

        在按照 [ [1] ] 安装完毕后，CMake 默认使用的 gcc 路径可能并不是新安装的 gcc，一种解决方法是在 CMake configure 时进行设置，需要重新执行上述的指令，在终端中输入：

        ```
        cmake . -B build -DSATSUMA_ENABLE_BLOSSOM5=0 -DCMAKE_C_COMPILER=***/bin/gcc -DCMAKE_CXX_COMPILER=***/bin/g++
        ```

        此处的 “ *** ” 需要替换为你实际新安装 gcc 的位置

        然后再执行：

        ```
        cmake --build build
        ```

## 测试

由于该项目是基于项目 **quadwild**，所以具体的使用说明类似 [nicopietroni/quadwild](https://github.com/nicopietroni/quadwild)

这里参考的是 [quadwild-bimdf/READMD](https://github.com/cgg-bern/quadwild-bimdf/blob/main/README.md)

1. 编译完成后得到的可执行文件位于 “quadwild-bimdf/build/Build/bin/”，进入该目录：

    ```
    cd xxx/quadwild-bimdf/build/Build/bin/
    ```

2. 将测试模型放置在该目录下，例如本文档目录下的 [jaw.obj](jaw.obj)
   
3. :bangbang: 然后需要回到 “quadwild” 根目录下（即需要 “config” 文件夹在该当前目录下），再执行后续的操作指令，不然后续操作中可能会找不到一些配置文件！（源于该方法中查找路径代码的缺陷）

4. 执行（具体输入模型的路径和名称根据实际情况而定）：

    ```
    ./build/Build/bin/quadwild build/Build/bin/jaw.obj 2 config/prep_config/basic_setup.txt
    ```

    执行完毕后，会生成一些过程结果

5. 再执行（具体输入过程模型的路径和名称根据实际情况而定）：

    ```
    ./build/Build/bin/quad_from_patches build/Build/bin/jaw_rem_p0.obj 123 config/main_config/flow_noalign_lemon.txt
    ```

6. 执行结束后会生成许多结果文件，其中 “jaw_rem_p0_123_quadrangulation.obj” 和 “jaw_rem_p0_123_quadrangulation_smooth.obj” （具体文件名称根据实际情况而定） 为最终结果

[1]: https://blog.csdn.net/qq_38308388/article/details/127574517