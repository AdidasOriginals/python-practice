#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/3 14:55 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_02.py
# @desc :数据结构和算法
# O(c)：常量时间复杂度 -  / 哈希存储
# O(log2n)：对数时间复杂度 - 折半查找（二分查找）
# O(n)：线性时间复杂度 - 顺序查找 / 计数排序
# O(n * log2n)：对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
# O(n2)：平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
# O(n3)：立方时间复杂度 - Floyd算法 / 矩阵乘法运算
# O(2n)：几何级数时间复杂度 - --汉诺塔
# O(n!)：乘阶时间复杂度 - 旅行经销商问题 - NPC
"""
查找 - 顺序查找和二分查找
算法：解决问题的方法（步骤）
评价一个算法的好坏主要有两个指标：渐近时间复杂度和渐近空间复杂度，通常一个算法很难做到时间复杂度和空间复杂度都很低（因为时间和空间是不可调和的矛盾）
表示渐近时间复杂度通常使用大O标记
O(c)：常量时间复杂度 - 哈希存储 / 布隆过滤器
O(log_2 n)：对数时间复杂度 - 折半查找
O(n)：线性时间复杂度 - 顺序查找
O(n * log_2 n)：- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
O(n ** 2)：平方时间复杂度 - 简单排序算法（冒泡排序、选择排序、插入排序）
O(n ** 3)：立方时间复杂度 - Floyd算法 / 矩阵乘法运算
也称为多项式时间复杂度
O(2 ** n)：几何级数时间复杂度 - 汉诺塔
O(3 ** n)：几何级数时间复杂度
也称为指数时间复杂度
O(n!)：阶乘时间复杂度 - 旅行经销商问题 - NPC
"""
print('排序算法（选择、冒泡和归并）和查找算法（顺序和折半）'.center(50, '*'))


def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        # 此处确定刚刚所排序好的最小值的次序
        min_index = i
        # # 此处range最大值为index最高位数+1, 因为遍历是从i+1开始和i对比
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


sort_list = [1, 55, 98984, 65, 165, 356, 54, 3, 645, 74, 64, 35, 666, 888]
print(f'原始数据：{sort_list}')
li = select_sort(sort_list)
print(f'简单选择排序后：{li}')


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if (comp(items[j], items[j + 1])):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


alist_old = [1, 55, 98984, 65, 165, 356, 54, 3, 645, 74, 64, 35, 666, 888]

alist_new = bubble_sort(alist_old)
print(f'简单选择排序后：{alist_new}')


def bubble_sort_new(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    for i in range(len(items) - 1):
        # 当已经排序好后，减少循环次数
        swapped = False
        # 正向：把当前循环最大的放到最后
        for j in range(len(items) - 1 - i):
            if (comp(items[j], items[j + 1])):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            # 反向：把当前循环最小的放到最前
            for j in range(len(items) - 2 - i, i, -1):
                if (comp(items[j - 1], items[j])):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


bubble_sort_list_old = [1, 55, 98984, 65, 165, 356, 54, 3, 645, 74, 64, 35, 666, 888]

bubble_sort_list = bubble_sort_new(bubble_sort_list_old)
print(f'搅拌排序后：{bubble_sort_list}')


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if (comp(items1[index1], items2[index2])):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10]
print(f'原始数据list_a:{list_a}')
print(f'原始数据list_b:{list_b}')
list_c = merge(list_a, list_b)
print(f'合并后排序：{list_c}')


# 归并排序：归并排序的思想就是先递归分解数组，再合并数组
def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    # 二分分解
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


merge_sort_list_old = [1, 55, 98984, 65, 165, 356, 54, 3, 645, 74, 64, 35, 666, 888]

merge_sort_list = merge_sort(merge_sort_list_old)
print(f'归并排序后：{merge_sort_list}')


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


seq_search_key = 888
seq_search_index = seq_search(sort_list, seq_search_key)
print(f'{seq_search_key}在list的坐标是：{seq_search_index}')


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


bin_search_key = 666
bin_search_index = bin_search(sort_list, bin_search_key)
print(f'{bin_search_key}在list的坐标是：{bin_search_index}')
# 穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
# 贪婪法 - 在对问题求解时，总是做出在当前看来
# 最好的选择，不追求最优解，快速找到满意解。
# 分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
# 回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
# 动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。
print('常用算法'.center(50, '*'))
print('穷举法例子：百钱百鸡和五人分鱼'.center(50, '*'))
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish = 6
while True:
    total = fish
    # 默认鱼的数量是够分的，enough = True
    enough = True
    # 循环步骤：每一个人都按照相同的原则分鱼
    # "_"符号在循环中不会用到，起的是循环次数的作用，可以看作和i,j是等效的
    for _ in range(5):
        # 如果正好够5个人分，不需要扔掉一条
        if (total - 1) % 5 == 0:
            # 除了第一个人，剩下的鱼的总数为：(total - 1) // 5 * 4，
            # 但是此时流程还没有走完，还未计算鱼的总数
            total = (total - 1) // 5 * 4
        # 如果不够一个人分，enough = False，
        # 说明鱼的数量不是最少的，还需要每一个重复步骤上加5条，跳出循环
        else:
            enough = False
            break
    # 判断鱼是不是够分，而且鱼的总数取的是最小值
    if enough:
        # 若是，输出鱼的总数，结束程序
        print(f'总共有{fish}条鱼')
        break
    # 鱼的数量循环加5
    fish += 5

print('贪婪法例子'.center(50, '*'))
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，
不追求最优解，快速找到满意解。
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品
"""
import prettytable

# 创建表
table = prettytable.PrettyTable()
# 添加表头
table.field_names = ['名称', '价格(美元)', '重量(kg)']
# 添加行数据
table.add_row(['电脑', 200, 20])
table.add_row(['收音机', 20, 4])
table.add_row(['钟', 175, 10])
table.add_row(['花瓶', 50, 2])
table.add_row(['书', 10, 1])
table.add_row(['油画', 90, 9])
print(table)
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


# if __name__ == '__main__':
#     main()
print('分治法例子：快速排序。'.center(50, '*'))
"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


quick_sort_list_old = [1, 55, 98984, 65, 165, 356, 54, 3, 645, 74, 64, 35, 666, 888]

quick_sort_list = quick_sort(quick_sort_list_old)
print(f'快速排序后：{quick_sort_list}')
print('回溯法例子：骑士巡逻。'.center(50, '*'))
"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，
比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
骑士巡逻，在一个棋盘中，有一个骑士，他是个骑士就会骑着马，众所周知，马走日，因此骑士巡逻的步骤就是：
骑士从棋盘中的某一点出发，按日字型的步伐遍历棋盘的每一个点而不重复
"""
import sys
import time

# 定义棋盘大小
SIZE = 5
# 定义一个全局变量，用于记录第total种巡游方式。
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    # 判断比较复杂
    # if row >= 0 and row < SIZE and \
    #         col >= 0 and col < SIZE and \
    #         board[row][col] == 0:
    # 简化之后
    if 0 <= row < SIZE and 0 <= col < SIZE and board[row][col] == 0:
        board[row][col] = step
        # 当最后一步恰好等于 25（本案例5*5）时，打印输出巡游路线
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'第{total}种走法：')
            print_board(board)
        #
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


# 马走日
#  23  12  3   18  25
#  4   17  24  13  8
#  11  22  7   2   19
#  16  5   20  9   14
#  21  10  15  6   1
def main1():
    # 生成5*5的棋盘
    board = [[0] * SIZE for _ in range(SIZE)]
    print(board)
    # 设定巡游起点为索引（4,4）
    patrol(board, SIZE - 1, SIZE - 1)


# if __name__ == '__main__':
#     main1()
print('动态规划例子：子列表元素之和的最大值。'.center(50, '*'))
"""子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，
可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值"""


def main2():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main2()
