# OpenMP 配置记录

本文档为配置 OpenMP 的记录

---

Canjia Huang <<canjia7@gmail.com>> last update 10/4/2025

# :apple: macOS

- 操作系统：macOS Sequoia 15.4 (M3)

## 配置步骤

1. 使用 Homebrew 安装 **llvm**：

    ```
    brew install llvm
    ```

1. 使用 Homebrew 安装 **libomp**：

    ```
    brew install libomp
    ```

2. 设置环境变量：

    ```
    vim ~/.zshrc
    ```

    在文件的最后添加：

    ```
    export CC=/opt/homebrew/Cellar/llvm/20.1.2/bin/clang
    export CXX=/opt/homebrew/Cellar/llvm/20.1.2/bin/clang++
    export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"
    ```

    保存并退出后，重新加载环境变量：

    ```
    source ~/.zshrc
    ```