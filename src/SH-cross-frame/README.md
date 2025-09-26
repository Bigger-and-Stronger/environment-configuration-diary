# SH-cross-frame 项目配置记录

本文档为配置文章 **"Boundary Aligned Smooth 3D Cross-Frame Field"** 的代码的记录 [[doi]](https://dl.acm.org/doi/abs/10.1145/2070781.2024177) [[exe]](http://www.cad.zju.edu.cn/home/hj/11/SH-cross-frame-1607-JiongCHEN.7z)

```
@article{10.1145/2070781.2024177,
    author = {Huang, Jin and Tong, Yiying and Wei, Hongyu and Bao, Hujun},
    title = {Boundary aligned smooth 3D cross-frame field},
    year = {2011},
    issue_date = {December 2011},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {30},
    number = {6},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/2070781.2024177},
    doi = {10.1145/2070781.2024177},
    journal = {ACM Trans. Graph.},
    month = dec,
    pages = {1–8},
    numpages = {8},
    keywords = {spherical harmonics, hexahedral, N-RoSy frame field}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 25/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 配置步骤

1. 将项目下载到本地：

    ```
    wget http://www.cad.zju.edu.cn/home/hj/11/SH-cross-frame-1607-JiongCHEN.7z
    ```

    下载完解压，或者在其他地方解压后再复制到服务器上

    然后进入目录：

    ```
    cd SH-cross-frame-1607-JiongCHEN
    ```

2. 进入 "bin" 目录并运行脚本：

    ```
    cd bin
    ./run_volume_frame.sh
    ```

    - :warning: 可能出现错误 `../sys/libc.so.6: version GLIBC_2.30 not found (required by /lib/x86_64-linux-gnu/libselinux.so.1)`

        参考 [hybrid-quad 项目配置记录](../hybrid-quad/) 中的解决方案，用系统中的已有的这些链接库来替换所提供的链接库

        ```
        cp /lib/x86_64-linux-gnu/libc.so.6 ../sys/libc.so.6
        ```

        后续可能会出现类似错误，都可以用类似方法解决

    - :warning: 可能出现错误 `./run_volume_frame.sh: line 30: 2299965 Segmentation fault      (core dumped) $FF_EXE prog=draw_3d_frame_sing tet=$MESH_FILE zyz=$ZYZ_FILE out=$SING_FILE`

        待解决

    - :warning: 在运行了可执行文件 `test_vol_frame` 后，终端中无输出，且输出目录 "../dat/sphere-ws1e0-wa1e3" 中是空的

        待解决
