# DirectionalFieldSynthesis 项目配置记录

本文档为配置文章 **"Directional Field Synthesis, Design, and Processing"** 的代码的记录 [[Doi]]( https://doi.org/10.1111/cgf.12864) [[Code]](https://github.com/avaxman/DirectionalFieldSynthesis)

```
@inproceedings{vaxman2016directional,
    title={Directional field synthesis, design, and processing},
    author={Vaxman, Amir and Campen, Marcel and Diamanti, Olga and Panozzo, Daniele and Bommes, David and Hildebrandt, Klaus and Ben-Chen, Mirela},
    booktitle={Computer graphics forum},
    volume={35},
    number={2},
    pages={545--572},
    year={2016},
    organization={Wiley Online Library}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 15/4/2025

:broken_heart: 该项目所依赖的两个关键的库 **libigl**、**Directional** 在后续版本中进行了较大修改，无法适配该项目

故不推荐编译该项目，可以直接使用 **Directional** 库，可以参考 [Directional 库配置记录](../Directional/)

如果仍然想要尝试配置该项目，可以查看该文档中已被注释的内容以解决部分问题

---

<!-- # :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [DirectionalFieldSynthesis/README](https://github.com/avaxman/DirectionalFieldSynthesis/blob/master/README.md)

1. 将项目下载到本地：

    ```
    git clone --recursive https://github.com/avaxman/DirectionalFieldSynthesis.git
    ```

    - :warning: 可能出现错误 `Fetched in submodule path 'demos/external/libdirectional', but it did not contain 35cad8f5171da5e781cc66afefceda987481822a. Direct fetching of that commit failed.`

        解决方法可以是重新手动下载该 submodule 项目：

        ```
        rm -rf DirectionalFieldSynthesis/demos/external/libdirectional/
        git clone https://github.com/avaxman/Directional.git DirectionalFieldSynthesis/demos/external/libdirectional/
        ```

    进入项目目录：

    ```
    cd DirectionalFieldSynthesis
    ```

该项目提供了 4 个 demos，编译过程如下

### demos/2-sampling

1. 进入想要编译的 demo 的目录，如：

    ```
    cd demos/2-sampling
    ```

2. 新建存放编译过程文件的目录：

    ```
    mkdir build
    ```

    并进入：

    ```
    cd build
    ```

3. 使用 CMake 进行 configure：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release ..
    ```

    - :warning: 可能出现错误 `libigl not found`

        在系统的某个目录下下载 **libigl** 库（如我是在用户根目录下）：

        ```
        git clone --recursive https://github.com/libigl/libigl.git
        ```

        并在上面的 CMake 指令中添加选项 `-DCMAKE_PREFIX_PATH=/home/huangcanjia/libigl/`，具体指定为下载的 **libigl** 目录

    - :warning: 可能出现错误 `libdirectional not found`

        该库下载到了 “DirectionalFieldSynthesis/demos/external/libdirectional/” 目录，同上添加相应的路径到 `-DCMAKE_PREFIX_PATH` 选项
    
    我实际执行的指令为：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/home/huangcanjia/libigl/:/home/huangcanjia/DirectionalFieldSynthesis/demos/external/libdirectional/ ..
    ```

:x: STILL FAILED... -->