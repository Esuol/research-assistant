# Agent 开发专家 SKILL

## 目的
当用户进入 phase4 多 Agent 项目时，提供专业的 Agent 设计和实现指导。

## 何时使用
- 用户在设计 Agent 架构
- 用户实现具体的 Agent（搜索、阅读、综合）
- 用户遇到 Agent 间的通信问题
- 用户需要理解 Agent Loop 的工作原理

## 核心概念速查

### Agent 的三个关键部分
1. **观察（Observation）** - Agent 看到什么信息？
2. **思考（Thought）** - Agent 如何理解这些信息？
3. **行动（Action）** - Agent 应该采取什么行动？

### 循环结构
```
观察 → 思考 → 决策 → 行动 → 新的观察 → ...（直到完成）
```

## 常见问题和解决方案

### ❌ 问题 1：Agent 无限循环
**症状：** Agent 一直重复相同的操作

**原因：**
- 没有定义清晰的停止条件
- Agent 判断自己还没完成

**解决：**
```python
# 添加最大迭代次数限制
max_iterations = 10

# 定义明确的完成条件
if task_complete:
    return result
```

### ❌ 问题 2：Token 溢出
**症状：** API 调用返回超出 Token 限制的错误

**原因：** 上下文积累太多

**解决：**
- 使用滑动窗口只保留最近的对话
- 实现摘要机制压缩历史
- 分块处理长文档

### ❌ 问题 3：Agent 之间干扰
**症状：** 多个 Agent 做重复工作或互相冲突

**原因：** 任务划分不清

**解决：**
- 为每个 Agent 定义明确的职责
- 使用消息格式标准化通信
- 建立协调器来分派任务

## 设计检查清单

进行 Agent 设计时，检查：

- [ ] 每个 Agent 的职责是否清晰？
- [ ] Agent 间的通信协议是否定义？
- [ ] 是否有明确的停止条件？
- [ ] 错误处理是否充分？
- [ ] 性能是否可以接受？
- [ ] 结果是否可追踪到源？

## 代码示例模式

### 搜索 Agent 的基本框架
```python
class SearchAgent:
    """搜索信息的 Agent"""
    
    def __init__(self, llm, search_tool):
        self.llm = llm
        self.search_tool = search_tool
    
    async def run(self, topic: str) -> list[dict]:
        """搜索并返回相关资源"""
        # 1. 思考：生成搜索关键词
        # 2. 行动：执行搜索
        # 3. 评估：是否满意结果？
        pass
```

## 测试 Agent 的方法

### 单元测试
```python
# 测试 Agent 的单一功能
def test_search_agent_finds_results():
    agent = SearchAgent(...)
    results = agent.search("Python")
    assert len(results) > 0
```

### 集成测试
```python
# 测试 Agent 间的协作
def test_full_pipeline():
    search_agent = SearchAgent(...)
    reading_agent = ReadingAgent(...)
    # 模拟完整流程
```

## 下一步建议

1. **先做小 Agent** - 搜索 Agent 最简单
2. **再做单独 Agent** - 阅读 Agent，但不连接
3. **最后协调** - 实现 Coordinator 来管理它们
