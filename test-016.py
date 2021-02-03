# coding=utf-8
print('*' * 10, '面向对象编程入门', '*' * 10)
print('-' * 10, '定义类', '-' * 10)


class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')


stu1 = Student()
stu2 = Student()
print(stu1)  # <__main__.Student object at 0x000001E26554A940>
print(stu2)  # <__main__.Student object at 0x000001E26554A8B0>
print(hex(id(stu1)), hex(id(stu2)))  # 0x1e26554a940 0x1e26554a8b0
# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')  # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu1.study('Python程序设计')  # 学生正在学习Python程序设计.
Student.play(stu2)  # 学生正在玩游戏.
stu2.play()  # 学生正在玩游戏.


class Student2:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}学生正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}学生正在玩游戏.')

    def __repr__(self):
        return f'{self.name}: {self.age}'


# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student2('测试', 40)
stu2 = Student2('王大锤', 15)
stu1.study('Python程序设计')
stu2.play()
print('-' * 10, '打印对象', '-' * 10)
stu1 = Student2('测试2', 40)
print(stu1)
students = [stu1, Student2('王大锤1', 16), Student2('王大锤2', 17)]
print(students)
print('-' * 10, '定义一个类描述数字时钟', '-' * 10)
import time


# 定义数字时钟类
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间-为0的时候补0空位长度2个"""
        # {self.hour:02d} 保留2位
        # {self.hour:0<2d} 左边补0  0可以换成X，Y，*
        # {self.hour:0>2d} 右边补0
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建时钟对象
clock = Clock(23, 59, 58)
# while True:
while False:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠1秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    clock.run()
print('-' * 10, '定义一个类描述平面上的点，要求提供计算到另一个点距离的方法', '-' * 10)


class Point(object):
    """屏面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'{self.x},{self.y}'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1, p2)
print(p1.distance_to(p2))
