#  在Windows11配置 ParSeNet/SED-Net 环境 | 踩坑记录
Shi Chen
29/11/2024 17:08

论文：
ParSeNet: A Parametric Surface Fitting Network for 3D Point Clouds,
Gopal Sharma, Difan Liu, Evangelos Kalogerakis, Subhransu Maji, Siddhartha Chaudhuri, Radomír Měch,
ECCV 2020.

[Paper](https://arxiv.org/pdf/2003.12181.pdf) | [Project Page](https://hippogriff.github.io/parsenet/) |[Code](https://github.com/Hippogriff/parsenet-codebase)

Surface and Edge Detection for Primitive Fitting of Point Clouds,
Yuanqi Li, Shun Liu, Xinran Yang, Jianwei Guo, Jie Guo, Yanwen Guo,
SIGGRAPH 2023 Conference Proceedings.

[Paper](https://dl.acm.org/doi/10.1145/3588432.3591522) | [Code](https://github.com/yuanqili78/SED-Net)

第二篇的方法简称SED-Net，环境是参照ParSeNet的环境配置，所以按理说配置了一个相当于能用于跑两篇论文的代码。ParSeNet仓库似乎没有预训练模型，而SED-Net提供了(不过只有带法向的版本)。不过我又在另一个工作 [Point2CAD](https://www.obukhov.ai/point2cad) [Li et al, 2024]的仓库中找到了[预训练好的ParSeNet模型](https://github.com/prs-eth/point2cad/tree/main/point2cad/logs/pretrained_models)。
## 一些准备

基础环境：大概流程参考李沐老师的视频配置conda环境

[Windows 下安装 CUDA 和 Pytorch 跑深度学习 - 动手学深度学习v2](https://www.bilibili.com/video/BV18K411w7Vs/?spm_id_from=333.999.0.0&vd_source=1cbae45260e0699477d7d3036009aa4f)

我使用的miniconda是老版本，可在miniconda[历史版本链接](https://repo.anaconda.com/miniconda/)中找到：
```
	Miniconda3-py310_23.11.0-2-Windows-x86_64
```

不确定其他版本是否会出现兼容问题。

## 克隆 GitHub 项目
1. 在开始菜单中搜索 "Anaconda Prompt" 或 "Miniconda Prompt" 并打开
2. 切换路径到你的工作页面，如D:\path\to\your\projects
```
	D:
	cd D:\path\to\your\projects
```
3. 克隆
```
	git clone https://github.com/Hippogriff/parsenet-codebase.git
```
4. 切换路径
```
	cd parsenet-codebase
```

## 配置环境

作者给的代码是`conda env create --force environment.yml -n parsenet
`，结合 [issues](https://github.com/Hippogriff/parsenet-codebase/issues/9) 里一位网友提供的信息，使用如下代码比较合适
```bash
	conda env create --file environment.yml -n parsenet
```
顺带一提，如果哪天你要把环境去除则输入：
```bash
	conda remove -n parsenet --all
```

在`environment.yml`中的配置比较老了，我配的时候经常出现版本问题。除此之外，SED-Net事实上还有一些依赖需要自己额外安装。下面是我调整后的文件内容，调整了一些版本信息，并添加了几个SED-Net的依赖：
```
name: parsenet
channels:
  - loopbio
  - defaults
  - pytorch
  - nvidia
  - conda-forge
  - anaconda
  - orbingol
dependencies:
  - python=3.7
  - numpy=1.21.0
  - pip
  - pip:
    - positional-encodings==6.0.1
    - lap==0.4.0
    - lapsolver==1.0.2
    - geomdl==5.2.9
    - h5py
    - open3d==0.16.0
    - scikit-image
    - scikit-learn
    - scipy
    - six==1.13.0
    - tensorboard-logger==0.1.0
    - torchvision==0.9.0
    - transforms3d==0.3.1
    - trimesh==2.31.38
    - pykdtree
    - configobj
    - matplotlib==3.5

```
该`.yml`可在本目录下找到，替换原始的`environment.yml`文件即可。

显示以下结果则说明成功！
```
#
# To activate this environment, use
#
#     $ conda activate parsenet
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

我在`environment.yml`中把torch去掉了，因为我自己pip安装torch时经常出现网络问题，因此在激活环境后使用conda单独安装。我的版本是1.8.0：
```
	conda activate parsenet
	conda install pytorch=1.8.0 cudatoolkit=11.1 -c pytorch
```


## 运行SED-Net
1. 克隆项目
```
	git clone https://github.com/yuanqili78/SED-Net.git
	cd SED-Net
```
2. 在 *SED-Net* 文件夹下创建 *ckpts，data，data_parsenet，predictions* 文件夹，并在 *predictions* 下创建四个文件夹。
```
	- SED-Net
		- ckpts
		- data
		- data_parsenet
		- predictions
			- config
			- gt
			- logs
			- results
```
3. 参考SED-Net的readme，将数据和预训练模型添加到文件夹中
- please download our dataset from [Onedrive](https://1drv.ms/f/s!AkbsfT9Y3igj3Hl9nmpQZsh7Vv5J?e=yOTZfe) or from [Baiduyun](https://pan.baidu.com/s/1apCmf8Xa_rXyRdWl4ybJpg?pwd=meta) (password is *meta*), and load all files of folder *sed_net_data* to *data* 
- please download parsenet datasets from [Onedrive](https://1drv.ms/f/s!AkbsfT9Y3igj3Hr1YQHzC8V0rO2-?e=XfwcSe) or from [Baiduyun](https://pan.baidu.com/s/16fggrr-qQRc2yu6ECQNaoA) (password is *meta*), and load all files of folder *parsenet* to *data_parsenet* 
- you can download our pretained models from [Onedrive](https://1drv.ms/f/s!AkbsfT9Y3igj3Hjl96WnhBMTAsWP?e=Akj76R) or from [Baiduyun](https://pan.baidu.com/s/1rMMD_0VaOGTmpMcIozjp3Q) (password is *meta*), and load all weights of folder *ckpts* to *ckpts*

4. 在数据集上测试模型
```
	python generate_predictions_aug.py configs/config_SEDNet_normal.yml NoSave no_multi_vote no_fold5drop
```
如果GPU显存不够，则在`generate_predictions_aug.py`中把HPNet编码选项改成不要。
``` bash
	... ... 
	HPNet_embed = False # ========================= default True 
	... ... 
```

## 测试自己的点云模型
由于SED-Net和ParseNet的默认代码都是处理点云数据集`h5`文件格式，而我们常见的点云都是`xyz`格式，即每行6个数值，前三个数值为点坐标，后三个为法向。
``` bash
	x0 y0 z0 nx0 ny0 nz0
	x1 y1 z1 nx1 ny1 nz1
	... ... 
```

在 *SED-Net*或*parsenet-codebase* 文件夹下创建 *xyz_file* 文件夹，存放自己的`xyz`文件。我把作者的代码简单改了一下，写了个`generate_seg_from_xyz.py`。将其放在*SED-Net*或*parsenet-codebase*文件夹下，开始运行：

``` bash
	python generate_seg_from_xyz.py configs/config_SEDNet_normal.yml NoSave no_multi_vote no_fold5drop
```

运行后*xyz_file* 文件夹下会出现`xyz`文件对应的`seg`文件。这个文件保存了模型的预测结果，即在之前的文件后面多加了两个数值，一个是分割ID，一个是基元类别ID。
``` bash
	x0 y0 z0 nx0 ny0 nz0 seg0 type0
	x1 y1 z1 nx1 ny1 nz1 seg1 type1
	... ... 
```