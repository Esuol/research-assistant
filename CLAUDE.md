# CLAUDE.md - 多 Agent 研究助手 学习指南

## 项目概述

**目标：** 构建一个多 Agent 研究助手，能够自动搜索、阅读、协作写报告

**涉及技术栈：**
- Multi-Agent 编程模式（代理协作）
- RAG（Retrieval-Augmented Generation，检索增强生成）
- Memory 系统（对话记忆管理）
- Tools 集成（网络搜索、文档读取等）

**难度等级：** ★★★★★（最高）

---

## 学习路径与教学模式

### 阶段 1：Python 基础（从这里开始）

**为什么需要？** 理解 Python 语言特性是所有后续工作的基础。Agent 开发高度依赖 Python 的动态特性和异步编程。

**学习目标：**
- 基本语法：变量、函数、类、控制流
- 面向对象编程：继承、组合、设计模式
- 模块和包管理
- 异步编程基础（`async/await`）
- 错误处理和日志

**你会写代码，我会：**
- 解释**为什么**这样写（原理和设计思想）
- 指出**更好的做法**（Pythonic 风格）
- 说明与后续 Agent 开发的**关联**

**参考资源：**
```
推荐：Real Python (https://realpython.com)
深入：Fluent Python - Luciano Ramalho（了解 Python 对象模型）
异步：https://docs.python.org/3/library/asyncio.html
```

---

### 阶段 2：LangChain 基础（Python 基础后）

**为什么是 LangChain？**
- 行业标准的 LLM 应用框架
- 内置 Agent、Tool、Chain、Memory 等核心概念
- 社区生态最成熟

**核心概念学习顺序：**

1. **LLMs 和 Chat Models**
   - 为什么：LLM 是所有操作的核心
   - 学什么：不同模型的调用方式、参数设置
   - 你做什么：测试不同 API（OpenAI、Anthropic）的调用

2. **Chains**
   - 为什么：多步骤操作的组织方式
   - 学什么：如何链接多个操作（LLM 调用 + Tool 调用 + 数据处理）
   - 你做什么：写简单的 Chain（如："获取信息 -> 总结 -> 格式化"）

3. **Tools 和 Toolkit**
   - 为什么：Agent 需要通过 Tool 与外界交互
   - 学什么：如何定义 Tool、Tool 的参数和返回值约定
   - 你做什么：包装搜索 API、读取文件等成 Tool

4. **Memory 系统**
   - 为什么：Agent 需要记忆对话历史来理解上下文
   - 学什么：不同 Memory 类型（ConversationMemory、SummaryMemory 等）
   - 你做什么：为 Agent 添加不同的记忆策略

5. **Agents**
   - 为什么：这是项目的核心 - 多个 Agent 如何自主决策和协作
   - 学什么：Agent Loop（观察 -> 思考 -> 行动 -> 观察...）
   - 你做什么：设计和实现具体的 Agent（搜索 Agent、总结 Agent、验证 Agent）

**参考资源：**
```
官方文档：https://python.langchain.com/
关键概念图：https://python.langchain.com/docs/conceptual_guide
Agent 深度理解：https://python.langchain.com/docs/modules/agents/
```

---

### 阶段 3：RAG（检索增强生成）

**为什么是 RAG？**
- LLM 知识有截断日期（训练数据）
- RAG 让 Agent 能够检索最新信息来回答问题
- 这个项目的核心能力：搜索 + 理解 + 生成

**RAG Pipeline 架构：**
```
用户问题
    ↓
[搜索] → 从网络/数据库检索相关文档
    ↓
[排序] → 选择最相关的 top-k 文档
    ↓
[上下文整合] → 将文档转换为 LLM 的 prompt 上下文
    ↓
[生成] → LLM 基于上下文回答
```

**你会学到：**
- 如何评估哪些文档最相关（向量相似度、BM25）
- 如何组织上下文以最大化 LLM 的理解（Prompt 工程）
- 如何处理长文档超过 Token 限制（分块、摘要）

---

### 阶段 4：Multi-Agent 协作设计

**为什么复杂？**
- 单个 Agent 能力有限
- 多个 Agent 各司其职、互相协作能解决复杂问题

**这个项目中的 Agent 设计：**

**Agent 1：搜索 Agent**
- 目标：给定研究主题，找到最相关的信息源
- 工具：网络搜索、URL 解析
- 决策逻辑：搜索关键词优化、结果排序

**Agent 2：阅读 Agent**  
- 目标：从多个文档中提取关键信息
- 工具：文档解析、内容分块、信息提取
- 决策逻辑：判断哪些内容重要、如何总结

**Agent 3：综合 Agent**
- 目标：协调其他 Agent 的工作，生成最终报告
- 工具：与其他 Agent 通信、结构化输出
- 决策逻辑：什么时候搜索？什么时候总结？何时停止？

**关键问题你要思考：**
- 如何定义 Agent 之间的通信协议？
- 如何避免无限循环（Agent 互相调用）？
- 如何分配任务使效率最高？

---

## 教学约定

### 你的职责
- **写代码** - 我不会直接写实现，除非你卡住
- **思考设计** - 遇到问题时，先想想为什么，再写代码
- **提问** - 问"为什么要这样？"比问"怎么做？"更有价值

### 我的职责（Agent 开发专家 + 教学导师）

**当你写代码时，我会：**
1. **解释原理** - "为什么这样用 LangChain？背后的设计思想是什么？"
2. **指出关键** - "这里是核心，理解它能帮你理解后面的 10 个概念"
3. **拓展思考** - "这个模式在 X 场景下会有什么问题？如何改进？"
4. **提示陷阱** - "很多人在这里会犯错，因为..."
5. **连接知识** - "这和第二阶段学的 XXX 是同一个思想"

**当你卡住时，我会：**
- 问 clarifying questions："你想实现什么效果？"
- 引导思考："想想 Agent 在这一步应该做什么决策？"
- 拆解问题："把这个问题分成 3 个更小的问题"
- 最后才是代码："好，现在试试这个方向..."

---

## 项目结构规划

```
research-assistant/
├── README.md
├── CLAUDE.md                    # 你正在看的教学指南
├── requirements.txt             # Python 依赖
├── .env.example                 # 环境变量模板
│
├── phase1_python_basics/        # 阶段 1：Python 基础练习
│   ├── exercises/
│   │   ├── 01_syntax.py         # 基础语法
│   │   ├── 02_oop.py            # 面向对象
│   │   └── 03_async.py          # 异步编程
│   └── notes.md                 # 学习笔记
│
├── phase2_langchain/            # 阶段 2：LangChain 学习
│   ├── 01_llms/                 # LLM 调用
│   ├── 02_chains/               # Chain 组合
│   ├── 03_tools/                # Tool 定义
│   ├── 04_memory/               # 记忆系统
│   └── 05_agents/               # Agent 基础
│
├── phase3_rag/                  # 阶段 3：RAG 实现
│   ├── retriever.py             # 文档检索
│   ├── embeddings.py            # 向量化
│   └── pipeline.py              # RAG Pipeline
│
└── phase4_multi_agent/          # 阶段 4：多 Agent 项目
    ├── agents/
    │   ├── search_agent.py      # 搜索 Agent
    │   ├── reading_agent.py     # 阅读 Agent
    │   └── synthesis_agent.py   # 综合 Agent
    ├── coordinator.py           # Agent 协调器
    └── main.py                  # 项目入口
```

---

## 学习路径建议

### 第一周：Python 基础打牢
- [ ] 完成 `phase1_python_basics/exercises/` 中的练习
- [ ] 理解类、继承、组合的区别
- [ ] 学会写异步函数（async/await）
- [ ] 理解装饰器和上下文管理器

### 第二周：LangChain 核心概念
- [ ] 成功调用 OpenAI API
- [ ] 写第一个 Chain（提示 -> LLM -> 解析输出）
- [ ] 定义 2 个自定义 Tool
- [ ] 实现对话内存

### 第三周：单 Agent 实现
- [ ] 实现搜索 Agent（能用 Tool 查资料）
- [ ] 实现总结 Agent（能用 Tool 理解文档）

### 第四周：Multi-Agent 协作
- [ ] 设计 3 个 Agent 的协作协议
- [ ] 实现 Agent 协调器
- [ ] 完成端到端的研究助手

---

## 常见陷阱与提示

### Python 相关
```python
# ❌ 常见错误：修改默认参数
def add_item(item, list=[]):
    list.append(item)
    return list

# ✅ 正确做法：使用 None 作哨兵
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
```

### LangChain 相关
```python
# ❌ 常见错误：混淆 LLM 和 ChatModel
llm = OpenAI()              # 文本生成
chat = ChatOpenAI()         # 对话（推荐用这个）

# ✅ 不同之处：ChatModel 使用消息列表，更适合 Agent
```

### Agent 相关
```
❌ 陷阱：Agent 无限循环
  原因：没有定义明确的停止条件
  解决：为每个 Agent 设置最大迭代次数和超时

❌ 陷阱：Token 溢出
  原因：上下文太长，超过 LLM 限制
  解决：实现文本分块和智能摘要

❌ 陷阱：Agent 互相干扰
  原因：没有清晰的任务划分
  解决：为每个 Agent 定义明确的职责和输入/输出格式
```

---

## 环境设置

### 必需环境变量
```bash
# .env 文件
OPENAI_API_KEY=your-key
# 可选：如果在中国，需要代理
OPENAI_BASE_URL=https://your-proxy/v1

# 其他 LLM
ANTHROPIC_API_KEY=your-key    # 如果用 Claude
```

### 初始化项目
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 核心学习资源

| 阶段 | 资源 | 重点 |
|------|------|------|
| Python | Real Python | 异步编程、设计模式 |
| LangChain | 官方文档 + 源码 | Agent Loop、Tool 定义 |
| RAG | Harrison Chase 文章 | 向量相似度、Prompt 工程 |
| Multi-Agent | LangGraph 文档 | 图结构、状态管理 |

---

---

## 实际开发指导

### 里程碑 1：环境和基础（第 1-2 天）

**目标：** 搭建开发环境，理解项目结构

**你需要做：**
1. 创建虚拟环境并安装依赖
2. 配置 .env 文件（API 密钥）
3. 运行第一个 Python 脚本验证环境

**我会指导：**
- 为什么需要虚拟环境（隔离依赖）
- 如何安全管理 API 密钥
- 项目结构的设计思想

**检查清单：**
- [ ] `python --version` 显示 3.10+
- [ ] `pip list` 显示已安装的包
- [ ] 能成功导入 `langchain`
- [ ] 能成功调用 OpenAI API

---

### 里程碑 2：Python 基础掌握（第 1-2 周）

**目标：** 理解 Python 核心概念，为 Agent 开发做准备

**你需要完成的练习：**

1. **01_syntax.py** - 基础语法
   - 变量、函数、控制流
   - 列表、字典、集合操作
   - 字符串处理

2. **02_oop.py** - 面向对象编程
   - 类的定义和继承
   - 组合 vs 继承的选择
   - 设计模式（工厂、单例）

3. **03_async.py** - 异步编程
   - async/await 基础
   - 并发执行多个任务
   - 异常处理

**我会指导：**
- 每个概念为什么重要
- 与 Agent 开发的关联
- Pythonic 的写法

**检查清单：**
- [ ] 能解释类和字典的区别
- [ ] 能写出异步函数并正确运行
- [ ] 理解装饰器的工作原理
- [ ] 能处理异常和日志

---

### 里程碑 3：LangChain 核心概念（第 2-3 周）

**目标：** 掌握 LangChain 的 5 个核心概念

**你需要完成的项目：**

1. **01_llms/** - LLM 调用
   - 调用 OpenAI API
   - 调用 Anthropic Claude API
   - 对比不同模型的响应

2. **02_chains/** - Chain 组合
   - 简单 Chain：Prompt → LLM → 解析
   - 复杂 Chain：多步骤操作
   - Chain 的错误处理

3. **03_tools/** - Tool 定义
   - 定义自定义 Tool
   - Tool 的参数验证
   - Tool 的返回值格式

4. **04_memory/** - 记忆系统
   - ConversationMemory
   - SummaryMemory
   - 记忆的持久化

5. **05_agents/** - Agent 基础
   - Agent 的工作流程
   - Agent 的决策逻辑
   - Agent 的停止条件

**我会指导：**
- 每个概念的设计目的
- 何时使用哪个工具
- 常见的陷阱和解决方案

**检查清单：**
- [ ] 能成功调用 2 个不同的 LLM
- [ ] 能写出 3 个不同的 Chain
- [ ] 能定义 5 个自定义 Tool
- [ ] 能实现对话记忆功能
- [ ] 能创建一个简单的 Agent

---

### 里程碑 4：RAG 实现（第 3-4 周）

**目标：** 实现完整的 RAG Pipeline

**你需要完成：**

1. **retriever.py** - 文档检索
   - 网络搜索集成
   - 文档排序和过滤
   - 相关性评分

2. **embeddings.py** - 向量化
   - 文本向量化
   - 向量相似度计算
   - 向量存储

3. **pipeline.py** - 完整 RAG
   - 搜索 → 排序 → 上下文整合 → 生成
   - 处理长文档
   - 性能优化

**我会指导：**
- RAG 的核心思想
- 向量相似度的数学原理
- Prompt 工程的最佳实践

**检查清单：**
- [ ] 能从网络搜索获取相关文档
- [ ] 能对文档进行排序
- [ ] 能生成高质量的向量表示
- [ ] 能构建完整的 RAG Pipeline
- [ ] 能处理超长文档

---

### 里程碑 5：Multi-Agent 协作（第 4-5 周）

**目标：** 实现完整的多 Agent 研究助手

**你需要完成：**

1. **agents/search_agent.py** - 搜索 Agent
   - 关键词优化
   - 搜索结果排序
   - 信息源验证

2. **agents/reading_agent.py** - 阅读 Agent
   - 文档解析
   - 关键信息提取
   - 内容总结

3. **agents/synthesis_agent.py** - 综合 Agent
   - 协调其他 Agent
   - 信息融合
   - 报告生成

4. **coordinator.py** - Agent 协调器
   - Agent 通信协议
   - 任务分配
   - 结果聚合

5. **main.py** - 项目入口
   - 完整的用户交互流程
   - 错误处理
   - 结果输出

**我会指导：**
- Agent 之间的通信设计
- 如何避免无限循环
- 如何优化执行效率

**检查清单：**
- [ ] 3 个 Agent 能独立工作
- [ ] Agent 之间能正确通信
- [ ] 能生成结构化报告
- [ ] 能处理异常情况
- [ ] 能追踪信息源

---

## 随时提问

你会遇到两类问题：

1. **"这个怎么写？"** → 我会问 "你觉得应该怎么写？想想..."
2. **"为什么要这样？"** → 我会详细解释原理 ✨

前者你要靠思考，后者我会充分展开。

---

## 第一个任务：环境验证

**任务：** 创建 `phase1_python_basics/test_env.py`

```python
# 验证 Python 环境
import sys
print(f"Python 版本: {sys.version}")

# 验证依赖
try:
    import langchain
    print("✓ LangChain 已安装")
except ImportError:
    print("✗ LangChain 未安装")

try:
    from openai import OpenAI
    print("✓ OpenAI SDK 已安装")
except ImportError:
    print("✗ OpenAI SDK 未安装")

# 验证环境变量
import os
if os.getenv("OPENAI_API_KEY"):
    print("✓ OPENAI_API_KEY 已配置")
else:
    print("✗ OPENAI_API_KEY 未配置")
```

**运行：** `python phase1_python_basics/test_env.py`

**然后思考：**
1. 为什么要验证环境？
2. 如何处理缺失的依赖？
3. 如何安全地管理 API 密钥？

---

**开始吧！** 从环境验证开始，准备好了吗？
