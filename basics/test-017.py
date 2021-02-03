# coding=utf-8
print('*' * 20, '面向对象编程进阶', '*' * 20)
print('-' * 10, '可见性和属性装饰器', '-' * 10)


# __name表示一个私有属性，_name表示一个受保护属性
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
# print(stu.__name) # 'Student' object has no attribute '__name'
print('-' * 10, '访问私有属性', '-' * 10)


class Student2:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}')


stu = Student2('王大锤', 20)
stu.study('Python程序设计')
print(stu._Student2__name, stu._Student2__age)
print('-' * 10, '访问私有属性', '-' * 10)


class Student3:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name

    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'

    @property
    def age(self):
        return self.__age


stu = Student3('王大锤', 20)
print(stu.name, stu.age)  # 王大锤 20
stu.name = ''
print(stu.name)  # 无名氏
# stu.age = 30   # AttributeError: can't set attribute
print('-' * 10, '动态属性', '-' * 10)


class Student4:
    # 不希望动态为对象添加属性，打开下面的方法
    # __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student4('王大锤', 20)
# 为Student对象动态添加sex属性
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'
print(stu.name, stu.age, stu.sex)
print('-' * 10, '静态方法和类方法', '-' * 10)


class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        self.a = c
        self.b = c
        self.c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # 类方法
    @classmethod
    def is_valid2(cls, a, b, c):
        """判断三条边长能否构成三角形(类方法)"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


print('是否能构成三角形:', Triangle.is_valid(10, 25, 30))
print('是否能构成三角形:', Triangle.is_valid2(10, 25, 30))
triangle = Triangle(15, 15, 15)
print('三角形的周长:', triangle.perimeter())
print('三角形的面积:', triangle.area())
print('-' * 10, '继承和多态', '-' * 10)


class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')


class Student5(Person):
    """学生类"""

    def __init__(self, name, age):
        # super(Student5,self).__init__(name,age)
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):
    def __init__(self, name, age, title):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}')


stu1 = Student5('李元芳', 21)
stu2 = Student5('狄仁杰', 22)
teacher = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
teacher.teach('Python程序设计')
stu1.study('Python程序设计')
