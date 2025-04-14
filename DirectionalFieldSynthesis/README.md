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

Canjia Huang <<canjia7@gmail.com>> last update 14/4/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

参考 [DirectionalFieldSynthesis/README](https://github.com/avaxman/DirectionalFieldSynthesis/blob/master/README.md)

1. 将项目下载到本地：

    ```
    git clone --recursive https://github.com/avaxman/DirectionalFieldSynthesis.git
    ```

    - :warning: 可能出现错误 `Fetched in submodule path 'demos/external/libdirectional', but it did not contain 35cad8f5171da5e781cc66afefceda987481822a. Direct fetching of that commit failed.`

        解决方法可以是之重新手动下载该 submodule 项目，先跳过该 submodule：

        ```
        
        ```
        
        执行：

        ```
        git clone https://github.com/avaxman/Directional.git DirectionalFieldSynthesis/demos/external/libdirectional/
        ```

    进入项目目录：

    ```
    cd DirectionalFieldSynthesis
    ```

2. 进入想要编译的 example 的目录，如：

    ```
    cd demos/2-sampling
    ```

3. 新建存放编译过程文件的目录：

    ```
    mkdir build
    ```

    并进入：

    ```
    cd build
    ```

4. 使用 CMake 进行 configure：

    ```
    cmake -DCMAKE_BUILD_TYPE=Release ../
    ```