# OpenFOAM 配置记录与基础操作

[OpenFOAM 官网](https://www.openfoam.com)
[OpenFOAM 官方api文档](https://api.openfoam.com/2306/)
[中文交流论坛（CFD中文网）](https://cfd-china.com/category/6/openfoam)

# :apple: macOS
Canjia Huang 24/2/2025 <<canjia7@gmail.com>>
- 操作平台：MacBook Air (Apple M3) - macOS 15.3
- OpenFOAM 版本：OpenFOAM-v2412

## 安装步骤
这里安装的是 [openfoam-app](https://github.com/gerlero/openfoam-app) ，有2种安装方式：

### 1. 直接使用 homebrew 安装
:bangbang: 这种安装方式非常方便，但是安装后 **OpenFOAM** 库的位置是位于挂载磁盘中的，使用终端执行操作不受影响，但若要自己编译求解器等时就无法再编译并写入（通过改变挂载磁盘的读写权限可能可以解决）
根据 [openfoam-app](https://github.com/gerlero/openfoam-app) 的 [README](https://github.com/gerlero/openfoam-app/blob/main/README.md) 中的步骤进行安装即可：
1. 安装 **Homebrew**
2. 终端中输入：
    `brew install --no-quarantine gerlero/openfoam/openfoam`

安装完成后，在启动台中会多出一个应用程序 **OpenFOAM-v2412.app**（具体名称取决于安装版本，这里均以此版本为例）

### 2. 根据源码编译安装（:+1: 推荐）
在 [openfoam-app](https://github.com/gerlero/openfoam-app) 的 [README Building from source](https://github.com/gerlero/openfoam-app/blob/main/README.md#-building-from-source) 中也有提到该安装方式：
1. 安装 [**pixi**](https://pixi.sh/latest/)，推荐用 **Homebrew** 安装（需先安装 **Homebrew**），在终端中输入：
   `brew install pixi`
   同时可能还需要安装 **Xcode Command Line Tools**，但我可能之前安装过所以并不需要
2. 将 **openfoam-app** 仓库git clone到本地，在终端输入：
    `git clone https://github.com/gerlero/openfoam-app.git`
3. 进入 **openfoam-app** 目录并编译：
   `pixi run make`

完成编译后在 openfoam-app/build 中会多出一个应用程序 **OpenFOAM-v2412.app**（该应用与使用 **Homebrew** 安装类似，库的位置也挂载于磁盘）
同时在 openfoam-app/build 下会出现一个磁盘文件 **OpenFOAM-v2412-build.sparsebundle**，打开后会挂载库的磁盘（如果已经挂载着磁盘，需要先将挂载着的磁盘推出），:floppy_disk: 此时挂载的磁盘是可编辑并写入的
   - 如果通过打开 **OpenFOAM-v2412-build.sparsebundle** 来挂载磁盘的情况下，可以通过打开挂载着的磁盘中的脚本 **openfoam** 来打开终端（该脚本的路径为：/Volumes/OpenFOAM-v2412/etc/**openfoam**）

如果只需要编译 **OpenFOAM-v2412-build.sparsebundle** 而不需要编译 **OpenFOAM-v2412.app**，可以将第3步中的编译命令改为执行：
`pixi run make build`

### Paraview 安装（:bulb: 可选）
OpenFOAM 可以通过 paraFoam 脚本来启动可视化软件 [paraview](https://www.paraview.org) 以可视化结果，同样可以使用 **Homebrew** 安装，根据 [brew/paraview](https://formulae.brew.sh/cask/paraview) 中步骤进行安装即可：
1. 安装 **Homebrew**
2. 终端中输入：
   `brew install --cask paraview`

## 入门操作（终端）
直接启动 **OpenFOAM-v2412.app**（或已经挂载磁盘的情况下启动磁盘中的脚本 etc/**openfoam**），会打开一个终端界面，可以在该终端界面中直接使用 OpenFOAM 的相关指令：
![](.pic/image1.png)
·
接下来可以通过具体案例测试一下，可以参考[官网相关文档-Examples](https://doc.openfoam.com/2312/examples/)
打开 **OpenFOAM-v2412.app** 后会挂载一个磁盘 **OpenFOAM-v2412**，该磁盘中 tutorials 目录下存放有一些测试案例
这里测试 /Volumes/OpenFOAM-v2412/tutorials/incompressible/pisoFoam/RAS/cavity 下的例子
 - OpenFOAM是将<u>要进行求解的问题</u>以及<u>求解器的参数</u>都存储在文件夹中的各个文件中，具体可以参考[官网相关文档-Quickstart](https://doc.openfoam.com/2312/quickstart/)，这里简要列出该案例的文件结构：
    ```
    cavity
        - 0.orig/ （包含在0时刻的初始/边界条件）
        - constant/ （包含定义着模拟中使用到的几何和物理性质的常数）
        - system/ （包含求解器参数和模拟工具等的设置）
        - Allclean （脚本）
        - Allrun （脚本）
        - Allrun-parallel （脚本）
    ```

:bangbang: 需要注意的是，如果你是通过打开 **OpenFOAM-v2412.app** 来开启终端的，此时挂载的磁盘没有读写权限，这会导致执行求解操作后生成的结果文件无法存储（可能可以通过改变磁盘的权限来解决），所以可以先将该案例文件夹复制到本地路径，我进行复制后的测试案例文件夹路径为：/Users/canjia/CFD/cavity
由于该案例已经包含 **Allrun** 脚本，可以通过执行该脚本来完成整个案例的测试（一般自己的案例可能要手动分几个步骤来完成，或自己编写 **Allrun** 脚本）
在 **OpenFOAM-v2412.app** 打开的终端中输入：
```
cd /Users/canjia/CFD/cavity
./Allrun
```

成功执行后会在 /Users/canjia/CFD/cavity 目录下生成许多求解结果相关的文件

如果已经安装了 **paraview**，可以对结果进行可视化，此时继续在 **OpenFOAM-v2412.app** 打开的终端中输入：
```
paraFoam
```

会自动打开 **Paraview**，可视化结果如下：
![](.pic/image2.png)

## 入门操作（C++）
[](https://www.cfd-online.com/Forums/openfoam-programming-development/241735-how-develop-openfoam-cmake-popular-ides.html)
[openfoam-cmake-app](https://github.com/kvns/openfoam-cmake-app)