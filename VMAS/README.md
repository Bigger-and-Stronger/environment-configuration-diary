# VMAS Windows11 环境配置
Shi Chen 
18/03/2025 20:29

本文配置以下论文的代码环境。
- Qijia Huang, Pierre Kraemer, Sylvain Thery, Dominique Bechmann. *"Dynamic Skeletonization Via Variational Medial Axis Sampling"*. 
  - SIGGRAPH Asia 2024 Conference Proceedings
  - [[Paper](https://huang46u.github.io/VMAS/static/pdfs/Dynamic_Skeletonization_via_Variational_Medial_Axis_Sampling.pdf)][[Project Page](https://huang46u.github.io/VMAS/)][[Code](https://github.com/huang46u/VMAS-code)]
  
:sunny: 该工作是讨论如何生成简化的中轴(或线面骨架)。
## 依赖
- Eigen
- Glfw3

Glfw3在Windows 11中可以用[vcpkg](https://github.com/microsoft/vcpkg)直接安装。这个项目还需要[CGOGN_3](https://github.com/cgogn/CGoGN_3)，但是作者已经将其需要的文件直接包含在仓库中。

## 配置
1. 克隆仓库:
   ```sh
   git clone git@github.com:huang46u/VMAS-code.git
   cd VMAS-code
   ```

2. CMake
   ```sh
   mkdir build
   cd build
   cmake ..
   ```

3. 生成

   打开Visual Studio，Release下右键vmas项目点击生成。

## 运行
在`data`中放置测试网格的`off`文件。

在`build`中运行代码，例如：
   ```sh
   ./stage/bin/Release/vmas.exe ../data/chair.off
   ```

此时会出现UI界面，会可视化中轴球的迭代过程，非常炫酷 :heart_eyes:！

但似乎在打开某些off文件时会卡死:dizzy_face:。