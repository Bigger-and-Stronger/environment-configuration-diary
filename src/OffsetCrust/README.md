# OffsetCrust 项目配置记录

本文档为配置文章 **"OffsetCrust: Variable-Radius Offset Approximation with Power Diagrams"** 的代码的记录 [[doi]](https://arxiv.org/abs/2507.10924) [[code]](https://github.com/zih-an/offsetcrust)

```
@misc{zhao2025offsetcrustvariableradiusoffsetapproximation,
      title={OffsetCrust: Variable-Radius Offset Approximation with Power Diagrams}, 
      author={Zihan Zhao and Pengfei Wang and Minfeng Xu and Shuangmin Chen and Shiqing Xin and Changhe Tu and Wenping Wang},
      year={2025},
      eprint={2507.10924},
      archivePrefix={arXiv},
      primaryClass={cs.GR},
      url={https://arxiv.org/abs/2507.10924}, 
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 12/10/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：
    ```
    git clone https://github.com/zih-an/offsetcrust.git
    ```

    进入项目目录：
    ```
    cd offsetcrust
    ```

2. 新建存放编译结果的目录并进入：
    ```
    mkdir build && cd build
    ```

3. 使用 CMake 进行 configure：
    ```
    cmake ..
    ```

    - :warning: 可能出现错误 `Could not find a package configuration file provided by "TBB" with any of the following names`

        需要安装 Intel TBB，具体可以参考 [TBB 库配置记录](../TBB/README.md)，然后设置 `CMAKE_PREFIX_PATH` 为 TBB 库的安装目录（具体路径根据实际情况而定）来进行 configure：
        ```
        cmake -DCMAKE_PREFIX_PATH=/home/huangcanjia/oneTBB/my_installed_onetbb/ ..
        ```

    - :warning: 可能出现错误 `Could not find a package configuration file provided by "nanoflann" with any of the following names`

        nanoflann 是一个仅头文件库，但此处可以进行安装：
        1. 在根目录下下载 nanoflann 库：
            ```
            git clone https://github.com/jlblancoc/nanoflann.git
            ```
            并进入目录：
            ```
            cd nanoflann
            ```
        2. 新建存放安装结果的目录：
            ```
            mkdir nanoflann-installed
            ```
        3. 新建存放编译结果的目录并进入：
            ```
            mkdir build && cd build
            ```
        4. 使用 CMake 进行 configure，并设置先前新建的目录为安装结果目录（具体路径根据实际情况而定）：
            ```
            cmake -DCMAKE_INSTALL_PREFIX=/home/huangcanjia/nanoflann/nanoflann-installed ..
            ```
        5. 编译：
            ```
            make -j
            ```
        6. 安装：
            ```
            make install
            ```

        安装完毕后，将 nanoflann 的安装目录添加到 CMake `CMAKE_PREFIX_PATH` 变量中进行 configure：

        ```
        cmake -DCMAKE_PREFIX_PATH=/home/huangcanjia/nanoflann/nanoflann-installed ..
        ```

    - :warning: 可能出现错误 `add_subdirectory given source "evaluation" which is not an existing directory.`

            注释掉 `offsetcrust/CMakeLists.txt` 的 Line 48，重新进行 configure 即可

4. 编译：
    ```
    make -j
    ```

## 测试步骤

编译成功后，在 `offsetcrust/build/variable3d` 和 `offsetcrust/build/constant3d` 目录下分别有可执行文件 `3DVer_variable` 和 `3DVer_constant`

由于可执行文件内部行为依赖于一些模型文件的相对路径，因此需要将它们复制到 `offsetcrust/data` 目录下

进入 `offsetcrust` 根目录，执行：
```
cp build/variable3d/3DVer_variable data/3DVer_variable
cp build/constant3d/3DVer_constant data/3DVer_constant
```

进入 `offsetcrust/data` 目录，执行：
```
./3DVer_constant --input "./2_robustness/fandisk.off" -d 0.02 --diag --outdir "./2_robustness/"
```
```
./3DVer_variable --input "./6_freeform/67855_sf.obj" --outdir "./6_freeform/" --dis "./6_freeform/chair.txt" --diag
```