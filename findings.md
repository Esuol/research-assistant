# 研究发现 - 多 Agent 研究助手 (阶段 1: Python 基础)

## 当前知识状态
- 已验证 Python 环境：Python 3.10+
- 已安装基础依赖：`langchain`, `openai` (通过 `test_env.py` 验证流程)
- 待学习重点：异步编程 (`asyncio`)、组合优于继承的设计思想、复杂字典/列表操作

## 技术发现
- **Agent 中的字符串处理**：在 Agent 开发中，字符串不仅仅是文本，通常是 Prompt 的组成部分或 JSON 的输入输出。因此，`word_frequency` 等练习是解析 LLM 响应的基础。
- **异常处理的必要性**：Agent 频繁调用网络 API，`safe_int_convert` 练习中的异常捕获逻辑将被直接应用于 API 超时或无效响应的处理。

## 待探索问题
- [ ] 如何在 Python 中高效地并发执行多个 Agent 调用？
- [ ] 组合 (Composition) 在 LangChain 工具定义中是如何体现的？
