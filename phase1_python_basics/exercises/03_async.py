import asyncio
import time

"""
Phase 1: Milestone 3 - 异步编程 (Asyncio)

底层逻辑：
在 Agent 开发中，网络请求（LLM API、搜索 API）是典型的 I/O 密集型任务。
如果你用同步 (Sync) 的写法，程序会卡在每一个 API 返回前，效率极低。
异步 (Async) 允许我们在等待 I/O 的同时，去处理其他任务，实现资源利用率的最大化。

任务目标：
1. 实现异步获取数据的 fetch_data 协程。
2. 使用 asyncio.gather 实现并发抓取。
3. 处理任务超时情况。
4. (可选进阶) 尝试实现一个异步生成器模拟流式输出。

抓手：
- async def 定义协程
- await 挂起当前协程，出让控制权
- asyncio.sleep 模拟非阻塞延迟
- asyncio.run 启动事件循环
"""

async def fetch_data(source: str, delay: int):
    print(f"[开始] 正在从 {source} 获取数据，预计耗时 {delay}s...")
    await asyncio.sleep(delay)
    result = f"{source} 数据内容"
    print(f"[完成] {source}")
    return result


async def main():
    start_time = time.perf_counter()

    print("--- 场景 1: 串行获取 (性能洼地) ---")
    t0 = time.perf_counter()
    r1 = await fetch_data("串行-A", 1)
    r2 = await fetch_data("串行-B", 2)
    print(f"串行结果: {r1!r}, {r2!r}，本子场景耗时: {time.perf_counter() - t0:.2f}s（约 1+2=3s）")

    print("\n--- 场景 2: 并发获取 (拉通效率) ---")
    t1 = time.perf_counter()
    results = await asyncio.gather(
        fetch_data("并发-1", 1),
        fetch_data("并发-2", 1),
        fetch_data("并发-3", 2),
    )
    print(f"并发结果: {results}，本子场景耗时: {time.perf_counter() - t1:.2f}s（约 max(1,1,2)=2s）")

    print("\n--- 场景 3: 超时控制 (风险防范) ---")
    try:
        await asyncio.wait_for(fetch_data("慢接口", 5), timeout=2.0)
    except asyncio.TimeoutError:
        print("[超时] 2s 内未完成，已取消慢任务（防范长阻塞）")

    end_time = time.perf_counter()
    print(f"\n[顶层对齐] 整个 Pipeline 执行完毕，总耗时: {end_time - start_time:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
