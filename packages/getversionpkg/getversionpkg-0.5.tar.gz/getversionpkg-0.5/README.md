# pi-package

#### 介绍
打包工具测试
 

#### 流程
要在Python中制作可以通过pip安装的包，你需要遵循一些步骤。以下是创建Python包并通过pip进行分发的基本步骤：
- 创建项目目录和初始文件。
- 编写代码。
- 设置setup.py。
- 版本控制。
- 打包和上传。

#### example

1. 创建一个目录和初始文件
   
   ```
    mkdir mypackage
    cd mypackage
    touch __init__.py
    touch mymodule.py
   ```
__init__.py 可以为空，但它告诉Python这是一个包。mymodule.py 是你的代码文件。

2. 编写代码 (mymodule.py)：
 ``` python
 # mymodule.py
def my_function():
    print("Hello from my package!")
```

3. 设置 `setup.py`

``` python
from setuptools import setup, find_packages
 
setup(
    name='mypackage',
    version='0.1',
    description='An example package',
    packages=find_packages(),
    python_requires='>=3.6',
)

```
4.创建一个 README.md 或 README.rst 文件，描述你的包。

5.创建 LICENSE 文件，指定包的许可证。

6.确保你有一个PyPI账户，并在 ~/.pypirc 中配置你的账户信息：
``` ini
[distutils]
index-servers = pypi
 
[pypi]
repository: https://upload.pypi.org/legacy/
username: your_username
password: your_password
```
7.打包你的包
```
python setup.py sdist bdist_wheel
```
8.上传
``` bash
twine upload dist/*
```
确保你已经安装了 setuptools 和 wheel，以及 twine，这是用于上传的工具。
完成这些步骤后，你的包就可以通过pip安装了。

9. 安装 
``` bash
pip install mypackage
pip install   getversionpkg -i https://pypi.org/simple
```

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

