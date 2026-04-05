# 验证 Python 环境
import sys
import os

def run_checks():
    print(f"Python 版本: {sys.version}")
    print("-" * 30)

    # 验证依赖
    dependencies = [
        ("langchain", "LangChain"),
        ("openai", "OpenAI SDK"),
        ("anthropic", "Anthropic SDK"),
        ("dotenv", "python-dotenv")
    ]

    for module_name, display_name in dependencies:
        try:
            __import__(module_name)
            print(f"✓ {display_name} 已安装")
        except ImportError:
            print(f"✗ {display_name} 未安装")

    print("-" * 30)

    # 验证环境变量
    env_vars = ["OPENAI_API_KEY", "OPENAI_BASE_URL", "ANTHROPIC_API_KEY"]
    for var in env_vars:
        value = os.getenv(var)
        if value:
            # 隐藏部分 key 以示安全
            masked_value = value[:6] + "..." + value[-4:] if len(value) > 10 else "***"
            print(f"✓ {var} 已配置: {masked_value}")
        else:
            print(f"✗ {var} 未配置")

if __name__ == "__main__":
    run_checks()
