# 多 Agent 研究助手 (Professional Edition)

这是一个面向专业研究场景的多 Agent 协作系统。它不仅仅是一个简单的聊天机器人，而是一个具备**自主搜索、深度阅读、结构化写作及自我校对**能力的工业级研究引擎。

## 🌟 核心产品形态与功能

### 1. 自主研究引擎 (Autonomous Research Engine)
- **多维度搜索策略**：Agent 自动将模糊的主题拆解为多个精确的搜索查询（Search Query Decomposition），覆盖学术、新闻、社交媒体等多个信息源。
- **深度链接爬取**：不局限于搜索摘要，阅读 Agent 会深入点击高价值链接，提取长篇文档内容。
- **动态任务编排**：基于 **LangGraph** 的图结构，Agent 会根据初步搜索结果动态决定是否需要补充搜索或深入研究某个子课题。

### 2. 知识萃取与 RAG 增强
- **智能分块与向量化**：支持 PDF, Markdown, HTML 等多种格式。
- **长文本上下文管理**：利用智能摘要技术，在有限的 Token 窗口内处理海量参考资料。
- **混合检索 (Hybrid Search)**：结合向量搜索（语义）和关键词搜索（精确），确保引用的准确性。

### 3. 专家级报告生成
- **多角色协作**：
    - **搜索专家 (Searcher)**：负责广度探索。
    - **分析专家 (Analyst)**：负责深度挖掘和逻辑梳理。
    - **主笔专家 (Writer)**：负责按学术或商务规范生成报告。
    - **审校专家 (Reviewer)**：负责对报告进行“幻觉检查”和事实校验。
- **全引用溯源**：报告中的每一个核心观点均带有点击可达的原始链接/文献引用。
- **多格式输出**：支持生成 Markdown, PDF, Word 格式。

### 4. 工业级观测与质量保证 (Expert Features)
- **全链路追踪 (Tracing)**：通过 LangSmith 可视化展示 Agent 的每一步思考（Chain of Thought）。
- **自动化评估 (Auto-Evals)**：内置 LLM-as-a-Judge 系统，自动评分报告的相关性、准确性和忠实度。
- **断点续传 (Checkpointing)**：支持超长研究任务的状态保存与恢复，无惧 API 异常。

---

## 🎯 实际应用场景 (Real-World Value)

为了使项目具备实际的生产力价值，本研究助手将针对以下三个垂直领域进行深度预设与优化：

### 1. 深度竞品分析 (Competitive Intelligence)
- **输入**：竞品公司名称 / 产品线
- **输出**：一份包含其最新市场动态、技术路线图（基于招聘和技术博客）、用户反馈趋势及优劣势对比的 SWOT 报告。
- **价值**：为产品经理和市场分析师节省 4-6 小时的人工搜集时间。

### 2. 行业趋势与白皮书摘要 (Industry Trend Digest)
- **输入**：某个新兴领域（如“钠离子电池”、“AI 智能体标准化”）
- **输出**：一份包含该领域近 6 个月内的投融资情况、政策导向、头部公司动作及技术突破点的深度摘要。
- **价值**：帮助投资经理和研究员快速跟进新领域。

### 3. 学术综述与论文初稿 (Academic Literature Review)
- **输入**：学术研究课题
- **输出**：检索 Arxiv、Semantic Scholar 等信息源，生成一份包含研究现状、核心算法对比及未来挑战的综述报告。
- **价值**：为科研人员提供高价值的文献索引和初步思路梳理。

---

## 🛠️ 工业级特性 (Value Multiplier)

为了让它成为一个可用的“产品”，我们将增加以下实用功能：
- **引文直达**：点击报告中的每个引用点，直接打开原始 PDF 或网页（解决 AI 幻觉的痛点）。
- **个性化风格模板**：支持“咨询公司风”、“学术严谨风”、“新闻简报风”等多种输出模版。
- **异步邮件发送**：研究任务完成后，自动将 PDF 报告发送到用户邮箱。
- **Slack/Discord 集成**：通过消息指令触发研究任务并接收简报。

---

## 🏗️ 系统架构

```
[ 用户输入 ] 
    ↓
[ Coordinator (LangGraph) ] ←─── [ Memory Pool ]
    ↓           ↑
    ├─→ [ Search Agent ] ──→ (Tavily/Google API)
    ├─→ [ Reader Agent ] ──→ (Playwright/RAG)
    └─→ [ Writer Agent ] ──→ (Structure Generator)
    ↓           ↑
[ Review Agent (Hallucination Check) ]
    ↓
[ Final Report (PDF/MD) ]
```

## 🛠️ 技术栈 (专家版)

- **核心框架**: LangGraph (状态机编排), LangChain
- **大模型**: Claude 3.5 Sonnet / GPT-4o
- **向量数据库**: Chroma / Pinecone
- **可观测性**: LangSmith / LangFuse
- **搜索工具**: Tavily AI / Serper
- **解析工具**: Unstructured.io (PDF 解析), Firecrawl (网页爬取)
- **部署**: Docker + FastAPI (后端), React + Tailwind (前端)

---

## 📈 职业路线对齐：Agent 专家

本项目的设计初衷是帮助开发者建立对 **LLM 应用工程化** 的深度理解，涵盖了目前 Agent 专家岗位的核心考点：
1. **状态管理** (LangGraph)
2. **评估闭环** (Evals)
3. **复杂 RAG 优化** (Hybrid Search, Re-ranking)
4. **Agent 鲁棒性** (Error Handling, Self-Reflection)

---

👉 **开发指南：** 参见 [CLAUDE.md](./CLAUDE.md)
👉 **当前计划：** 参见 [task_plan.md](./task_plan.md)
