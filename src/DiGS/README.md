# DiGS: Divergence guided shape implicit neural representation for unoriented point clouds 环境配置

*Xiaoyang Yu, 2025-8-9*

### 🐧 Linux
平台：Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-125-generic x86_64)

---

### 配置

这是一篇有关配置文章 "*DiGS: Divergence guided shape implicit neural representation for unoriented point clouds*" 的记录。[文章主页](https://chumbyte.github.io/DiGS-Site/) | [代码仓库](https://github.com/Chumbyte/DiGS?tab=readme-ov-file)


配置：依次输入以下命令


    $ git clone https://github.com/Chumbyte/DiGS.git

    $ cd DiGS/

    $ conda create -n digs python=3.7.9 

    $ conda activate digs

在 pip 安装前，把 `requirements.txt` 中的 `open3d==0.11.2`，替换为 `open3d==0.13.0`


    $ pip install -r requirements.txt

    $ conda install -c plotly plotly plotly-orca

    $ conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia

    $ pip install protobuf==3.20.3


---

### 测试

作者提供了一个二维形状测试脚本，无需外部数据


    $ cd sanitychecks

    $ chmod +x ./scripts/run_train_test_basic_shape.sh

    $ ./scripts/run_train_test_basic_shape.sh


### 可能的报错

```cmd
Collecting sklearn
  Downloading sklearn-0.0.post12.tar.gz (2.6 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [15 lines of output]
      The 'sklearn' PyPI package is deprecated, use 'scikit-learn'
      rather than 'sklearn' for pip commands.
      
      Here is how to fix this error in the main use cases:
      - use 'pip install scikit-learn' rather than 'pip install sklearn'
      - replace 'sklearn' by 'scikit-learn' in your pip requirements files
        (requirements.txt, setup.py, setup.cfg, Pipfile, etc ...)
      - if the 'sklearn' package is used by one of your dependencies,
        it would be great if you take some time to track which package uses
        'sklearn' instead of 'scikit-learn' and report it to their issue tracker
      - as a last resort, set the environment variable
        SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True to avoid this error
      
      More information is available at
      https://github.com/scikit-learn/sklearn-pypi-package
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
```

原因：open3d 库版本过低，寻找依赖 sklearn（现在已经更名为 scikit-learn ）的时候报错

解决方法：把 `requirements.txt` 中的 `open3d==0.11.2`，替换为 `open3d==0.13.0`

---

```cmd
Traceback (most recent call last):
  File "test_basic_shape.py", line 6, in <module>
    import basic_shape_dataset2d
  File "/home/yuxiaoyang/DiGS/sanitychecks/basic_shape_dataset2d.py", line 6, in <module>
    import utils.visualizations as vis
  File "/home/yuxiaoyang/DiGS/utils/visualizations.py", line 7, in <module>
    import utils.utils as utils
  File "/home/yuxiaoyang/DiGS/utils/utils.py", line 4, in <module>
    from tensorboardX import SummaryWriter
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/__init__.py", line 5, in <module>
    from .torchvis import TorchVis
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/torchvis.py", line 11, in <module>
    from .writer import SummaryWriter
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/writer.py", line 17, in <module>
    from .comet_utils import CometLogger
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/comet_utils.py", line 7, in <module>
    from .summary import _clean_tag
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/summary.py", line 13, in <module>
    from .proto.summary_pb2 import Summary
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/proto/summary_pb2.py", line 16, in <module>
    from tensorboardX.proto import tensor_pb2 as tensorboardX_dot_proto_dot_tensor__pb2
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/proto/tensor_pb2.py", line 16, in <module>
    from tensorboardX.proto import resource_handle_pb2 as tensorboardX_dot_proto_dot_resource__handle__pb2
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/tensorboardX/proto/resource_handle_pb2.py", line 42, in <module>
    serialized_options=None, file=DESCRIPTOR),
  File "/home/yuxiaoyang/.conda/envs/digs/lib/python3.7/site-packages/google/protobuf/descriptor.py", line 561, in __new__
    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

More information: https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
```

原因：protobuf版本太高

解决方法：

    $ pip install protobuf==3.20.3
