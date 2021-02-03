# coding=utf-8
print('*' * 20, '面向对象编程应用', '*' * 20)
print('-' * 10, '扑克游戏', '-' * 10)
from enum import Enum


# 扑克4个花色
class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


for suite in Suite:
    print(f'{suite}:{suite.value}')


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        # suites = ['♠','♥','♣','♦']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)  # ♠5
print(card2)  # ♥K

import random


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


poker = Poker()
poker.shuffle()  # [♦2, ♣5, ♣7, ♥8, ♦4, ♦8, ♣J, ♣K, ♥J, ♥A, ♣8, ♠6, ♠J, ♦7, ♥9, ♠A, ♠10, ♥6, ♦3, ♠9, ♦K, ♥2, ♣2, ♣A, ♥5, ♠Q, ♣3, ♦J, ♦10, ♠8, ♠7, ♣6, ♦A, ♥Q, ♥4, ♦5, ♣10, ♣4, ♥K, ♦6, ♣9, ♣Q, ♠4, ♥3, ♦9, ♠K, ♥7, ♦Q, ♠2, ♥10, ♠5, ♠3]
print(poker.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


# 创建四个玩家并将牌发到玩家的手上
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    # TypeError: '<' not supported between instances of 'Card' and 'Card'
    # 2个card对象不能比较，需要再Card类中添加__lt__ 比较方法 lt---<  le---<= gt---> ge--->=  eq---== ne---!=
    player.arrange()
    print(f'{player.name}:', end='')
    print(player.cards)
print('-' * 10, '工资结算系统', '-' * 10)
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05


emps = [
    Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'),
    Programmer('荀彧'), Salesman('吕布'), Programmer('张辽')
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间;'))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额:'))
    print(f'{emp.name}本月工资为:¥{emp.get_salary():.2f}元')
