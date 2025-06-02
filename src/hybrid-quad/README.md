# hybrid-quad 项目配置记录

本文档为配置文章 **"Quadrangulation through Morse-Parameterization Hybridization"** 的代码的记录 [[Paper]](https://dl.acm.org/doi/abs/10.1145/3197517.3201354) [[Jin Huang]](http://www.cad.zju.edu.cn/home/hj/index.xml) [[exe]](http://www.cad.zju.edu.cn/home/hj/18/hybrid_quad_binary_Mint19_V20180731.7z)

```
@article{10.1145/3197517.3201354,
    author = {Fang, Xianzhong and Bao, Hujun and Tong, Yiying and Desbrun, Mathieu and Huang, Jin},
    title = {Quadrangulation through morse-parameterization hybridization},
    year = {2018},
    issue_date = {August 2018},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    volume = {37},
    number = {4},
    issn = {0730-0301},
    url = {https://doi.org/10.1145/3197517.3201354},
    doi = {10.1145/3197517.3201354},
    journal = {ACM Trans. Graph.},
    month = jul,
    articleno = {92},
    numpages = {15},
    keywords = {quadrangulation, periodic vector fields, parameterization, morse-smale complex, frame fields}
}
```

---

Canjia Huang <<canjia7@gmail.com>> last update 28/3/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.5 LTS

## 配置记录

1. 新建目录并进入：

    ```
    mkdir hybrid-quad
    cd hybrid-quad
    ```

2. 该项目没有提供源码，但提供了可执行文件，可以下载到本地：

    ```
    wget http://www.cad.zju.edu.cn/home/hj/18/hybrid_quad_binary_Mint19_V20180731.7z
    ```

    并解压（使用 **p7zip** 解压，具体安装流程可以见 [p7zip 配置记录](../p7zip/)）：

    ```
    7zz x hybrid_quad_binary_Mint19_V20180731.7z
    ```

    可以删除原压缩包文件：

    ```
    rm hybrid_quad_binary_Mint19_V20180731.7z
    ```

## 测试

参考该压缩包内提供的 “readme.txt” 文件

1. 进入目录：

    ```
    cd script
    ```

2. 项目中有内置测试模型，可以运行：

    ```
    bash run.sh aircraft-m
    ```

    - :warning: 可能出现错误 `../so/libc.so.6: version 'GLIBC_2.30' not found`

        可能是因为系统版本太高导致的，无权限的情况下不好解决，有权限的情况下也不好解决，容易出问题，所以可以不解决

        主要影响了 “hybrid-quad/script/run.sh” 中的 `mkdir` 指令和 `sed` 指令，这些指令的执行不成功导致后续的代码执行出错

        可以尝试用系统的链接库替换 “hybrid-quad/so/” 中的某些链接库：

        ```
        cp /lib/x86_64-linux-gnu/libc.so.6 ../so/libc.so.6
        cp /lib/x86_64-linux-gnu/libpthread.so.0 ../so/libpthread.so.0
        cp /lib/x86_64-linux-gnu/librt.so.1 ../so/librt.so.1
        ```

        我在配置过程中只需要替换以上三个文件即可成功运行，如果有其他链接库出现问题也可以按照类似方法在系统中寻找替换

    - :warning: 可能出现错误 `run.sh: line 79: ../test/output/aircraft-m/LOG_CHECK_aircraft-m.txt: No such file or directory`

        该问题是由于 “hybrid-quad/script/run.sh” 脚本没有成功使用 'mkdir' 指令创建目录导致的，具体解决方法参考上一个错误 :warning: 的解决方案

    - :warning: 可能出现错误 `An error occurred in MPI_Init_thread`，包括 `opal_shmem_base_select failed`, `opal_init failed`, `ompi_mpi_init: ompi_rte_init failed` 等错误

        可能是 **OpenMPI** 的版本与该编译程序不一致导致的，**OpenMPI** 库的安装可以参考 [OpenMPI 库配置记录](../OpenMPI/)








        cp -v /home/huangcanjia/openmpi-5.0.7/openmpi-installed/lib/*mpi*.so.* /home/huangcanjia/hybrid-quad/so/