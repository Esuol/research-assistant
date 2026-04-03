# 多 Agent 研究助手

自动化研究工具：给定一个研究主题，系统自动搜索、阅读、分析资料，多个 Agent 协作生成专业研究报告。

## 项目目标

**核心能力：** 从"研究主题" → "最终报告"的完整自动化流程

```
用户输入研究主题
    ↓
[搜索 Agent] 找到相关资料 (网络搜索)
    ↓
[阅读 Agent] 提取关键信息 (文档解析、内容理解)
    ↓
[综合 Agent] 协调整合、生成报告 (多源信息融合)
    ↓
输出：结构化研究报告
```

## 最终功能清单

### 核心功能
- [ ] **搜索能力** - 给定关键词，自动搜索网络获取相关资源
- [ ] **阅读能力** - 解析 URL 内容，提取关键信息和数据
- [ ] **理解能力** - 用 LLM 分析文档，生成摘要和洞察
- [ ] **记忆能力** - 保存对话历史，支持多轮交互
- [ ] **协作能力** - 多个 Agent 分工协作，避免重复工作

### 输出格式
- [ ] **结构化报告** - 包含：摘要、关键发现、数据支撑、参考资源
- [ ] **可追溯性** - 每个观点都能追踪到原始资源
- [ ] **可配置性** - 支持自定义报告深度、长度、风格

### 高级功能（可选）
- [ ] **增量研究** - 基于已有报告继续深化研究
- [ ] **对比分析** - 多个主题的对比研究
- [ ] **实时更新** - 监控新资源并更新报告

## 技术栈

| 层级 | 技术 | 用途 |
|------|------|------|
| **LLM** | Claude / OpenAI | 核心推理引擎 |
| **框架** | LangChain / LangGraph | Agent 编排 |
| **搜索** | Tavily / Google Search API | 网络搜索 |
| **解析** | BeautifulSoup / Playwright | 网页内容提取 |
| **存储** | SQLite / JSON | 对话和报告存储 |
| **语言** | Python 3.10+ | 后端实现 |

## 学习路径

详见 [CLAUDE.md](./CLAUDE.md) - 包含完整的教学指南和学习里程碑。

**快速开始：**
```bash
# 1. 环境设置
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，填入 API 密钥

# 3. 运行第一个练习
python phase1_python_basics/exercises/01_syntax.py
```

## 项目结构

```
research-assistant/
├── README.md                    # 项目概览（你在这里）
├── CLAUDE.md                    # 详细教学指南
├── requirements.txt             # Python 依赖
├── .env.example                 # 环境变量模板
│
├── 📚 学习铺垫（阶段 1-4）
│   ├── phase1_python_basics/    # 阶段 1：Python 基础
│   │   ├── exercises/           # 练习题
│   │   ├── solutions/           # 参考解答
│   │   └── tests/               # 单元测试
│   │
│   ├── phase2_langchain/        # 阶段 2：LangChain 学习
│   │   ├── 01_llms/             # LLM 调用
│   │   ├── 02_chains/           # Chain 组合
│   │   ├── 03_tools/            # Tool 定义
│   │   ├── 04_memory/           # 记忆系统
│   │   └── 05_agents/           # Agent 基础
│   │
│   ├── phase3_rag/              # 阶段 3：RAG 实现
│   │   ├── retriever.py
│   │   ├── embeddings.py
│   │   └── pipeline.py
│   │
│   └── phase4_multi_agent/      # 阶段 4：多 Agent 项目
│       ├── agents/
│       ├── coordinator.py
│       └── main.py
│
├── 🚀 实际项目代码
│   ├── backend/                 # Python 后端
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── venv/
│   │
│   └── frontend/                # 前端代码
│       ├── src/
│       ├── package.json
│       └── node_modules/
```

**说明：**
- **学习铺垫（phase1-4）** - 按照 CLAUDE.md 的教学路径，逐步学习 Python、LangChain、RAG、Multi-Agent
- **实际项目（backend/frontend）** - 最终的研究助手产品代码

## 学习时间估计

| 阶段 | 内容 | 时间 | 产出 |
|------|------|------|------|
| 1 | Python 基础 | 1-2 周 | 3 个练习 + 理解 |
| 2 | LangChain | 2-3 周 | 5 个小项目 |
| 3 | RAG | 1-2 周 | 完整 RAG Pipeline |
| 4 | Multi-Agent | 2-3 周 | 完整研究助手 |
| **总计** | | **6-10 周** | **可用产品** |

## 教学模式

- **你的职责：** 写代码、思考设计、提问
- **我的职责：** 解释原理、指出关键、引导思考

详见 CLAUDE.md 中的"教学约定"部分。

## 快速参考

### 常见命令
```bash
# 运行特定阶段的练习
python phase1_python_basics/exercises/01_syntax.py

# 运行测试
pytest phase1_python_basics/tests/

# 检查代码质量
pylint phase1_python_basics/

# 格式化代码
black phase1_python_basics/
```

### 调试技巧
- 使用 `python -m pdb` 进行交互式调试
- 使用 `logging` 模块记录执行流程
- 使用 `asyncio.run()` 测试异步函数

## 资源链接

- [LangChain 官方文档](https://python.langchain.com/)
- [Python 异步编程](https://docs.python.org/3/library/asyncio.html)
- [Real Python](https://realpython.com/)
- [LangGraph 文档](https://langchain-ai.github.io/langgraph/)

## 下一步

👉 **开始学习：** 打开 [CLAUDE.md](./CLAUDE.md)，从"第一个任务"开始！
