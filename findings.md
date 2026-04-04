# 研究发现 - 多 Agent 研究助手 (阶段 1: Python 基础)

## 当前知识状态
- 已验证 Python 环境：Python 3.10+
- 已安装基础依赖：`langchain`, `openai` (通过 `test_env.py` 验证流程)
- 待学习重点：异步编程 (`asyncio`)、组合优于继承的设计思想、复杂字典/列表操作

## 专家级洞察 (应聘 Agent 专家加分项)

- **为什么需要评估 (Evals)?**：在面试中，如果你能说出“我不仅仅做了一个 Agent，我还建立了一套评估指标（如忠实度、相关性、幻觉率）来量化它的性能”，这直接让你脱颖而出。
- **状态管理的重要性**：单向的 Chain 是脆弱的。真正的专家会使用**图结构 (Graph)**。当搜索 Agent 发现资料不足时，它应该能主动“退回”给综合 Agent 要求重新搜索。
- **Token 经济学**：在高阶开发中，你需要关注 Context Window 的利用率。如何通过长短期记忆管理（Memory Management）在保证效果的同时降低成本。
- **错误恢复 (Self-Correction)**：Agent 如果能识别自己的工具调用失败并重试（Self-Reflection），这是区分初级和高级开发者的分水岭。
- [ ] 如何在 Python 中高效地并发执行多个 Agent 调用？
- [ ] 组合 (Composition) 在 LangChain 工具定义中是如何体现的？
