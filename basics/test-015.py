# coding=utf-8
print('*' * 10, '常用数据结构之字典', '*' * 10)
print('-' * 10, '创建字典', '-' * 10)
xinhua = {
    '麓': '山脚下', '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名', '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)
# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)  # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}
# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print(items2)
# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print(len(person))
for key in person:
    print(key)
print('-' * 10, '字典的运算', '-' * 10)
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
# 检查name和tel两个键在不在person字典中
print('name' in person, 'tel' in person)  # True False
# 通过age修将person字典中对应的值修改为25
if 'age' in person:
    person['age'] = 25
# 通过索引操作向person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '测试'
print('name' in person, 'tel' in person)  # True True
# 检查person字典中键值对的数量
print(len(person))
# 对字典的键进行循环并通索引运算获取键对应的值
for key in person:
    print(f'{key}:{person[key]}')
print('-' * 10, '字典的方法', '-' * 10)
# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}
# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1002))  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(students.get(1005))  # None
print(students.get(1005, {'name': '无名氏'}))  # {'name': '无名氏'}
# 获取字典中所有的键
# dict_keys([1001, 1002, 1003])
print(students.keys())
# 获取字典中所有的值
# dict_values([{'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}, {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}, {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}])
print(students.values())
# 获取字典中所有的键值对
# dict_items([(1001, {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}), (1002, {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}), (1003, {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'})])
print(students.items())
# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '------>', value)
# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print(stu1)  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(len(students))  # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)  # {}
# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()
print(key, value)  # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
# setdefault可以更新字典中的键对应的值或向字典中存入新的键值对
# setdefault方法的第一个参数是键，第二个参数是键对应的值
# 如果这个键在字典中存在，更新这个键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
print(result)  # {'name': '方启鹤', 'sex': True}
print(students)  # {1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}, 1005: {'name': '方启鹤', 'sex': True}}
# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(
    students)  # {1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}, 1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'}, 1010: {'name': '王语嫣', 'sex': False, 'age': 19}, 1008: {'name': '钟灵', 'sex': False}}
person = {'name': '王大锤', 'age': 25, 'sex': True}
del person['age']
print(person)  # {'name': '王大锤', 'sex': True}
print('-' * 10, '字典的应用', '-' * 10)
# sentence = input('请输入一段话:')
sentence = 'QQQQWWWEEEERRRR'
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次')
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
