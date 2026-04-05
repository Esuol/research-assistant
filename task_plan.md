# 任务规划 - 多 Agent 研究助手 (Python 专家之路)

## 目标
利用已有的 TS 经验，快速打通 Python 生态下的 Multi-Agent 架构，重点攻克 LangGraph 状态机与 Evals 评估体系。

## 阶段规划

### 阶段 1: Python 工程化基础 (已对齐)
- [x] Pythonic 语法习惯养成 (`01_syntax.py`)
- [x] OOP vs Composition 深度理解 (`02_oop.py`)
- [ ] **异步并发流水线** (`03_async.py`)：这是 Agent 响应速度的**抓手**。

### 阶段 2 & 3: LangChain & RAG (已在 TS 中掌握)
- [x] 核心概念拉通：Retriever, Chain, Memory (跳过)

### 阶段 4: Multi-Agent 协作设计 (深度实战)
- [ ] **通信协议 Schema**：基于 Pydantic 定义 Agent 间的消息契约。
- [ ] **子任务编排器 (Planner)**：实现类似 AutoGPT 的任务拆解逻辑。
- [ ] **Tool 动态绑定**：实现根据上下文动态为 Agent 分配 Toolset。

### 阶段 5: LangGraph 状态机与长效记忆 (核心/进阶)
- [ ] **循环流 (Cycles)**：实现“自审视”回路，不合格的结果退回重做。
- [ ] **状态持有 (Thread State)**：实现多轮对话中的复杂状态管理。
- [ ] **Time-travel/Debugging**：实现状态回溯，精确定位 Agent 思考偏差。

### 阶段 6: 评估、观测与安全 (专家加分项)
- [ ] **LLM-as-a-Judge**：编写专门的评分 Agent 评价研究报告。
- [ ] **Tracing 与可视化**：集成 LangSmith 观测所有 Token 消耗。
- [ ] **代码执行沙箱**：基于 Docker 或 WASM 的安全执行环境。

## 决策日志
- **2026-04-05**: 根据用户反馈，调整路径：跳过已掌握的 TS 对应部分，将重心转向 **Python 异步并发**、**LangGraph 复杂状态机** 和 **工业级 Evals**。
