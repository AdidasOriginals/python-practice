#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/5 16:04 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_04.py
# @desc : 面向对象相关知识
print('工资结算系统'.center(50, '*'))
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '管理者'),
        EmployeeFactory.create('P', '搬砖的', 120),
        EmployeeFactory.create('P', '打工人', 85),
        EmployeeFactory.create('S', '销售者', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


main()
print('扑克游戏'.center(50, '*'))
"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
from enum import Enum, unique
import random


@unique
class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    # 输出对象的信息 repr() 函数将对象转化为供解释器读取的形式
    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（随机乱序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)


def main1():
    """主函数"""
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)


main1()
print('对象的复制（深复制/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆）垃圾回收、循环引用和弱引用'.center(50, '*'))
# 循环引用会导致内存泄露 - Python除了引用技术还引入了标记清理和分代回收
# 在Python 3.6以前如果重写__del__魔术方法会导致循环引用处理失效
# 如果不想造成循环引用可以使用弱引用
list1 = []
list2 = []
list1.append(list2)
list2.append(list1)
# 调用gc.collect()
# gc模块的计数器达到阀值
# 程序退出
print('多重继承'.center(50, '*'))
"""
多重继承 - 一个类有两个或者两个以上的父类
MRO - 方法解析顺序 - Method Resolution Order
当出现菱形继承（钻石继承）的时候，子类到底继承哪个父类的方法
Python 2.x - 深度优先搜索
Python 3.x - C3算法 - 类似于广度优先搜索
"""


class A():
    def say_hello(self):
        print('Hello A')


class B(A):
    pass


class C(A):
    def say_hello(self):
        print('Hello C')


class D(B, C):
    pass


# python2.x 新式类，所有类都要继承obejct，需要在创建类时继承object，经典类，在定义基类时，如果继承object才是新式类，否则是经典类
# Python 3中只存在新式类
# （Method Resolution Order，方法解析顺序）  经典类自左向右的深度遍历，新式类自左向右的广度遍历
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())
# python 类有多继承特性，如果继承关系太复杂，很难看出会先调用那个属性或方法。
# 为了方便且快速地看清继承关系和顺序，可以用__mro__方法来获取这个类的调用顺序。
print(D.__mro__)
D().say_hello()


class X(object): pass


class Y(object): pass


class E(X): pass


class F(Y): pass


class G(E, F): pass


# [<class '__main__.G'>, <class '__main__.E'>, <class '__main__.X'>, <class '__main__.F'>,
# <class '__main__.Y'>, <class 'object'>]
print(G.mro())

print('自定义字典限制只有在指定的key不存在时才能在字典中设置键值对'.center(50, '*'))


class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict = SetOnceDict()
try:
    # try捕获了异常，不会报错，直接set两次会报错
    my_dict['username'] = '吴彦祖'
    my_dict['username'] = '彭于晏'
except KeyError:
    pass
print(my_dict)
print('元编程和元类'.center(50, '*'))
# 对象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。
# 所有的类都直接或间接的继承自object，所有的元类都直接或间接的继承自type
print('用元类实现单例模式'.center(50, '-'))
"""
元 - meta
元数据 - 描述数据的数据 - metadata
元类 - 描述类的类 - metaclass - 继承自type
"""
import threading


# 单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
# 开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
# 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
# 里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
# 接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
# 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
# 最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息
class SingletonMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """总统(单例类)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """主函数"""
    p1 = President('特朗普', 'USA')
    p2 = President('奥巴马', 'USA')
    p3 = President.__call__('克林顿', 'USA')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


main()
print('可插拔的哈希算法（策略模式）'.center(50, '*'))
"""
哈希摘要 - 数字签名/指纹 - 单向哈希函数（没有反函数不可逆）
应用领域：
1. 数据库中的用户敏感信息保存成哈希摘要
2. 给数据生成签名验证数据没有被恶意篡改
3. 云存储服务的秒传功能（去重功能）
"""

# 创建型模式：单例、工厂、建造者、原型
# 结构型模式：适配器、门面（外观）、代理
# 行为型模式：迭代器、观察者、状态、策略
class StreamHasher():
    """摘要生成器"""

    def __init__(self, algorithm='md5', size=4096):
        """初始化方法
        @params:
            algorithm - 哈希摘要算法
            size - 每次读取数据的大小
        """
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()

    def digest(self, file_stream):
        """生成十六进制的摘要字符串"""
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main1():
    """主函数"""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('../basic/data/a.txt', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


main1()
