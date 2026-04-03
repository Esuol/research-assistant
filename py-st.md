## 虚拟环境
python3 -m venv venv
source venv/bin/activate
# 备注：创建虚拟环境目录 `venv/`（用于隔离依赖）。之后用 `pip install` 装的包只会进这个环境。
# 备注：激活虚拟环境后，当前终端里的 `python`/`pip` 会切换到 `venv/bin/` 下的版本；退出用 `deactivate`。

## 常用命令
python --version
# 备注：查看当前 python 版本；如果你的系统同时有 python2/3，建议用 `python3 --version` 或确认你已经激活虚拟环境。

python3 --version
# 备注：直接查看 Python3 版本（不依赖当前激活状态）。

which python
# 备注：查看当前使用的 python 路径；激活虚拟环境后通常会指向 `venv/bin/python`。

python path/to/xxx.py
# 备注：运行指定 Python 脚本。

python -m module_name
# 备注：用“模块方式”运行（常用于 `pip`、`venv` 等内置/标准模块）。

## 安装依赖
pip install package_name
# 备注：在当前激活的虚拟环境里安装第三方包。

pip install -r requirements.txt
# 备注：根据 `requirements.txt` 批量安装依赖（通常在新建/换环境后使用）。

pip freeze > requirements.txt
# 备注：把当前环境已安装的包导出到 `requirements.txt`（用于“同步依赖”）。

## requirements 相关
pip show package_name
# 备注：查看某个包的版本、安装位置等信息。

## 运行与开发
python -i path/to/xxx.py
# 备注：运行后进入交互模式，方便继续调试变量。

python -m pdb path/to/xxx.py
# 备注：用调试器 pdb 单步调试（遇到报错时很有用）。

## 环境管理
deactivate
# 备注：退出当前虚拟环境，回到系统默认 python。

## 快速步骤

- 1. 创建项目目录
mkdir my-new-project
cd my-new-project
- 2. 初始化虚拟环境
python3 -m venv venv
source venv/bin/activate
- 3. 创建 requirements.txt
# 列出你需要的包
# 比如：
# langchain>=0.1.0
# openai>=1.3.0
# python-dotenv>=1.0.0
- 4. 安装依赖
pip install -r requirements.txt
- 5. 创建 .env 文件
cp .env.example .env
# 编辑 .env，填入 API 密钥



