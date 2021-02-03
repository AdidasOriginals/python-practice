# coding=utf-8
print('*' * 10, '常用数据结构之集合', '*' * 10)
print('-' * 10, '创建集合', '-' * 10)
# 创建集合的字面量语法(重复元素不会出现在集合中)
set1 = {1, 2, 3, 3, 2, 1}
print(set1)
print(len(set1))
# 创建集合的构造器语法(后面会讲到什么是构造器)
set2 = set('hello')
print(set2)
# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)
# 创建集合的生成式语法(将列表生成式的[]换成{})
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)
# 集合元素的循环遍历
for elem in set4:
    print(elem)
print('-' * 10, '成员运算', '-' * 10)
set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(15 in set1)
set2 = {'Python', 'Java', 'Go', 'Swift'}
print('Ruby' in set2)
print('Java' in set2)
print('-' * 10, '交并差运算', '-' * 10)
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
# 交集   {2, 4, 6}
# 方法一: 使用 & 运算符
print(set1 & set2)  # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2))  # {2, 4, 6}
# 并集   {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法一: 使用 | 运算符
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用union方法
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 差集   {1, 3, 5, 7}
# 方法一: 使用 - 运算符
print(set1 - set2)  # {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2))  # {1, 3, 5, 7}
# 对称差   {1, 3, 5, 7, 8, 10}
# 方法一: 使用 ^ 运算符
print(set1 ^ set2)  # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2))  # {1, 3, 5, 7, 8, 10}
# 集合的交集、并集、差集运算还可以跟赋值运算一起构成复合运算
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
# 将set1和set2求并集再赋值给set1
# 也可以通过set1.update(set2)来实现
set1 |= set2
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
# 将set1和set3求交集再赋值给set1
# 也可以通过set1.intersection_update(set3)来实现
set1 &= set3
print(set1)  # {3, 6}
print('-' * 10, '比较运算', '-' * 10)
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2
# <运算符表示真子集，<=运算符表示子集
print(set1 < set2, set1 <= set2)  # True True
print(set2 < set3, set2 <= set3)  # False True
# 通过issubset方法也能进行子集判断
print(set1.issubset(set2))  # True
# 反过来可以用issuperset或>运算符进行超集判断
print(set2.issuperset(set1))  # True
print(set2 > set1)  # True
set1 = []
# set2的子集是<=   [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# set2的真子集是<   [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
set2 = [1, 2, 3]
print(set1 < set2)  # True
print(set1 <= set2)  # True


def getRealSubSet(list_demo):
    sub_list_all = []  # 用于存放集合所有的子集
    for i in range(1 << len(list_demo)):  # 循环遍历0到2**n之间的每个数
        combo_list = []  # 用于存放每个单独的循环中取出的子集
        for j in range(len(list_demo)):
            if i & (1 << j):  # 每一个数用&操作判断改为上是否有1
                combo_list.append(list_demo[j])  # 有的话保存起来
        sub_list_all.append(combo_list)
    return sub_list_all


print(getRealSubSet([1, 2, 3]))
print('-' * 10, '集合的方法', '-' * 10)
# 创建一个空集合
set1 = set()
# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})
# {33, 1, 100, 55, 1000, 10}
print(set1)
# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
# {1, 10, 33, 55, 1000}
print(set1)
# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 10 in set1:
    set1.remove(10)
# {33, 1, 55, 1000}
print(set1)
# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())
# clear方法可以清空整个集合
set1.clear()
# set()
print(set1)
# 判断两个集合有没有相同的元素可以使用isdisjoint方法，没有相同元素返回True，否则返回False
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True
print('-' * 10, '不可变集合', '-' * 10)
set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
# frozenset({1, 3, 5})
print(set1 & set2)
# frozenset({1, 2, 3, 4, 5, 7})
print(set1 | set2)
# frozenset({7})
print(set1 - set2)
# False
print(set1 < set2)
