# Neural-Singular-Hessian 环境配置

*Xiaoyang Yu, 2025-8-8*

### 🐧 Linux
平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

### 配置

这是一篇有关配置文章 "*Neural-Singular-Hessian: Implicit Neural Representation of Unoriented
Point Clouds by Enforcing Singular Hessian*" 的记录。[文章主页](https://www.bearprin.com/publications/neural-singular-hessian23wang/) | [代码仓库](https://github.com/bearprin/Neural-Singular-Hessian)

代码仓库中给出的测试环境为 Python 3.8, torch 1.31.1, CUDA 11.6 on Ubuntu 18.04

配置：依次输入以下命令


    $ git clone https://github.com/bearprin/Neural-Singular-Hessian.git

    $ cd Neural-Singular-Hessian/

    $ conda env create -f env.yaml 

    $ conda activate neural_singular


---

### 测试

作者提供了一个运行脚本，会重建 `./data/sdf/input` 路径下的所有 `*.xyz， *.ply` 文件


    $ cd surface_reconstruction

    $ python run_sdf_recon.py


### 可能的报错

```cmd
Traceback (most recent call last):
  File "train_surface_reconstruction.py", line 69, in <module>
    vis.plot_cuts_iso(net.decoder, save_path=os.path.join(output_dir, str(batch_idx) + '.html'))
  File "/home/yuxiaoyang/Neural-Singular-Hessian/utils/visualizations.py", line 104, in plot_cuts_iso
    fig.write_html(save_path)
  File "/home/yuxiaoyang/.conda/envs/neural_singular/lib/python3.8/site-packages/plotly/basedatatypes.py", line 3700, in write_html
    return pio.write_html(self, *args, **kwargs)
  File "/home/yuxiaoyang/.conda/envs/neural_singular/lib/python3.8/site-packages/plotly/io/_html.py", line 536, in write_html
    path.write_text(html_str)
  File "/home/yuxiaoyang/.conda/envs/neural_singular/lib/python3.8/pathlib.py", line 1256, in write_text
    return f.write(data)
UnicodeEncodeError: 'ascii' codec can't encode character '\xb1' in position 126938: ordinal not in range(128)
```

解决方法：把 `./utils/visualizations.py` 104 行 `fig.write_html(save_path)`，替换为

```
html_str = fig.to_html()
with open(save_path, 'w', encoding='utf-8') as f:
    f.write(html_str)
```
