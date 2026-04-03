import sys
import os

from dotenv import load_dotenv
load_dotenv()

print(f"Python 版本: {sys.version}")


# 检查 langchain 和 openai 是否安装
try:
    import langchain  # noqa: F401

    print("langchain: 已安装")
except ImportError:
    print("langchain: 未安装")

try:
    import openai  # noqa: F401

    print("openai: 已安装")
except ImportError:
    print("openai: 未安装")


# 检查 OPENAI_API_KEY 是否设置
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("OPENAI_API_KEY: 已设置（不会打印具体值，避免泄露）")
else:
    print("OPENAI_API_KEY: 未设置（请在 shell 或 .env 中配置）")

# 检查 OPENAI_BASE_URL 是否设置（代理用户需要）
base_url = os.getenv("OPENAI_BASE_URL")
if base_url:
    print(f"OPENAI_BASE_URL: 已设置为 {base_url}")
else:
    print("OPENAI_BASE_URL: 未设置（如需代理，请配置）")

