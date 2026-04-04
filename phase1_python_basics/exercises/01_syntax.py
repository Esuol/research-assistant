"""
阶段 1 练习 1：Python 基础语法

目标：理解 Python 的基本语法和数据结构

你需要完成的任务：
1. 定义变量和基本类型
2. 写函数处理列表和字典
3. 使用控制流（if/for/while）
4. 处理异常
"""

# 任务 1：变量和基本类型
# 定义一个函数，接收一个数字，返回它的平方
def square(n):
    """返回 n 的平方"""
    return n ** 2


# 任务 2：列表操作
# 定义一个函数，接收一个列表，返回去重后的列表（保持顺序）
def remove_duplicates(items):
    """
    使用 dict.fromkeys() 去重并保持顺序
    这是 Python 3.7+ 中最 Pythonic 的做法
    """
    return list(dict.fromkeys(items))


# 任务 3：字典操作
# 定义一个函数，接收一个字典列表，返回按指定键排序的结果
def sort_by_key(items, key):
    """
    items: [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    key: "age"
    返回: 按 age 排序的列表
    """
    pass


# 任务 4：字符串处理
# 定义一个函数，接收一个句子，返回单词频率字典
def word_frequency(sentence):
    """
    sentence: "hello world hello"
    返回: {"hello": 2, "world": 1}
    """
    pass


# 任务 5：异常处理
# 定义一个函数，安全地将字符串转换为整数
def safe_int_convert(value):
    """
    如果转换成功，返回整数
    如果失败，返回 None 并打印错误信息
    """
    pass


if __name__ == "__main__":
    # 测试你的实现
    print("测试 square(5):", square(5))
    print("测试 remove_duplicates([1,2,2,3]):", remove_duplicates([1, 2, 2, 3]))
    print("测试 word_frequency('hello world hello'):", word_frequency("hello world hello"))
    print("测试 safe_int_convert('123'):", safe_int_convert("123"))
    print("测试 safe_int_convert('abc'):", safe_int_convert("abc"))
