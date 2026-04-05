"""
02_oop.py - 面向对象编程

目标：理解类、继承、组合和设计模式

关键概念：
- 为什么用类？（封装状态和行为）
- 继承 vs 组合（什么时候用哪个？）
- 单一职责原则（SRP）
"""

# 任务 1：定义一个基础类
# 创建一个 Person 类，表示一个人
class Person:
    """
    属性：
    - name: 姓名
    - age: 年龄

    方法：
    - __init__: 初始化
    - __str__: 字符串表示
    - is_adult: 判断是否成年
    - grow: 增加年龄
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def is_adult(self) -> bool:
        return self.age >= 18

    def grow(self, years: int = 1):
        self.age += years


# 任务 2：继承
# 创建 Student 类，继承 Person
class Student(Person):
    """
    额外属性：
    - student_id: 学号
    - gpa: 绩点

    额外方法：
    - update_gpa: 更新绩点
    """

    def __init__(self, name: str, age: int, student_id: str, gpa: float = 0.0):
        super().__init__(name, age)
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        return f"Student {self.name} ({self.age}), id={self.student_id}, gpa={self.gpa}"

    def update_gpa(self, new_gpa: float):
        if not 0 <= new_gpa <= 4:
            raise ValueError("gpa 必须在 0 到 4 之间")
        self.gpa = new_gpa


class Teacher(Person):
    """教师，供工厂 create_person(..., 'teacher') 使用。"""

    def __init__(self, name: str, age: int, subject: str = ""):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        subj = self.subject or "未指定科目"
        return f"Teacher {self.name} ({self.age}), {subj}"


# 任务 3：组合优于继承
# 为什么 Student 不该继承 Person，而是应该包含一个 person？
# 创建一个 Student 类（使用组合方式）

class StudentComposed:
    """
    使用组合的方式：
    - 包含一个 Person 对象
    - 持有自己的 student_id 和 gpa
    """

    def __init__(self, name: str, age: int, student_id: str, gpa: float = 0.0):
        self._person = Person(name, age)
        self.student_id = student_id
        self.gpa = gpa

    def get_name(self):
        return self._person.name


# 任务 4：设计模式 - 工厂模式
# 创建一个工厂函数，根据类型创建不同的 Person 对象

def create_person(person_type: str, name: str, age: int, **kwargs) -> Person:
    """
    person_type: "person", "student", "teacher"
    根据类型创建不同的对象
    """
    kind = person_type.lower().strip()
    if kind == "person":
        return Person(name, age)
    if kind == "student":
        sid = kwargs.get("student_id")
        if sid is None:
            raise ValueError("创建 student 需要关键字参数 student_id")
        return Student(name, age, sid, float(kwargs.get("gpa", 0.0)))
    if kind == "teacher":
        return Teacher(name, age, str(kwargs.get("subject", "")))
    raise ValueError(f"不支持的 person_type: {person_type!r}")


if __name__ == "__main__":
    # 测试你的实现
    p = Person("Alice", 30)
    print(p)
    print(f"成年人? {p.is_adult()}")

    s = Student("Bob", 20, "S12345")
    print(s)
    s.update_gpa(3.8)
