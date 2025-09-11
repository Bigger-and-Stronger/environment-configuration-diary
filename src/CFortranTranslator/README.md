# CFortranTranslator 配置记录

本文档为配置项目 **CFortranTranslator** 的记录 [[code]](https://github.com/CalvinNeo/CFortranTranslator)，该工具用于将一个 Fortran 语言文件转换为 C++ 语言文件

---

Canjia Huang <<canjia7@gmail.com>> last update 11/9/2025

# :penguin: Ubuntu

- 操作系统：Ubuntu 20.04.6 LTS

## 预备步骤

安装 **bison**，具体可参考 [[bison 配置记录]](../bison/)

## 配置步骤

1. 将项目下载到本地：

    ```
    git clone https://github.com/CalvinNeo/CFortranTranslator.git
    ```

    并进入项目目录：

    ```
     cd CFortranTranslator
    ```

2. 进入 build 目录：

    ```
    cd build
    ```
3. 编译：

    ```
    make
    ```

    - :warning: 可能出现错误 `../for90std/forlang.h:176:16: error: ‘INT8_MAX’ was not declared in this scope^~~~~~~~`

        编译器一般也已经给出了解决方案，即在 `CFortranTranslator/for90std/forlang.h` 文件的开头添加头文件 `#include <cstdint>`，添加后重新进行编译

4. 编译完成后，会在 `build` 目录下生成可执行文件 **CFortranTranslator**
   
5. （可选）如果是 root 用户，可以执行安装指令以将该应用安装到系统目录：

    ```
    make install
    ```