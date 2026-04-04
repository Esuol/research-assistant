# 任务规划 - 多 Agent 研究助手 (阶段 1: Python 基础)

## 目标
掌握 Python 核心编程能力，为后续 LangChain 和 Multi-Agent 开发打下坚实基础。

## 阶段规划

### 阶段 1: 基础语法 (进行中)
- [ ] 完成 `exercises/01_syntax.py` 中的所有任务
  - [x] `square`: 变量与基本类型
  - [x] `remove_duplicates`: 列表操作
  - [ ] `sort_by_key`: 字典操作
  - [ ] `word_frequency`: 字符串处理
  - [ ] `safe_int_convert`: 异常处理
- [ ] 通过代码审查和测试验证

### 阶段 2: 面向对象编程 (待开始)
- [ ] 完成 `exercises/02_oop.py` 中的所有任务
  - [ ] `Person` 类定义
  - [ ] `Student` 继承实现
  - [ ] `StudentComposed` 组合实现
  - [ ] 工厂模式实现

### 阶段 3: 异步编程 (待开始)
- [ ] 创建并完成 `exercises/03_async.py`
  - [ ] `async/await` 基础
  - [ ] `asyncio.gather` 并发
  - [ ] 异步异常处理

### 阶段 4: Multi-Agent 协作设计 (待开始)
- [ ] 设计 3 个 Agent 的协作协议
- [ ] 实现 Agent 协调器
- [ ] 完成端到端的研究助手

## 🚀 专家进阶阶段 (致敬应聘目标)

### 阶段 5: Agent 评估与观测 (Evals & Observability)
- [ ] **LLM-as-a-Judge**: 实现自动化的报告评分系统
- [ ] **Tracing**: 集成 LangSmith 或 LangFuse，可视化 Agent 的思考链路
- [ ] **RAG 评估**: 使用 Ragas 评估检索准确率和生成忠实度

### 阶段 6: 复杂架构与长效记忆 (Advanced Architecture)
- [ ] **LangGraph 状态机**: 将 Agent 协作从简单的 Chain 升级为图结构（支持循环和回退）
- [ ] **持久化 Checkpoints**: 实现研究进度的断点续传（如果 API 挂了，下次能从中间继续）
- [ ] **Human-in-the-loop**: 在 Agent 生成最终报告前增加“人工确认/干预”环节

### 阶段 7: 工具沙箱与安全性 (Safety & Tooling)
- [ ] **Python 代码执行沙箱**: 让阅读 Agent 能够写 Python 代码来处理数据
- [ ] **信息源验证**: 自动检查网页的真实性和权威性评分

## 决策日志
- **2026-04-04**: 启动项目规划，使用 `planning-with-files` 系统跟踪进度。优先完成基础语法练习。
