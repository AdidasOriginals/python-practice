# coding=utf-8
print('*' * 10, '列表和元组的应用', '*' * 10)
print('-' * 10, '成绩表和平均分统计', '-' * 10)
# 录入5个学生3门课程的考试成绩,计算每个学生的平均分和每门课的平均分
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 用生成式创建嵌套的列表保存5个学生3门课程的成绩
scores = [[0] * len(courses) for _ in range(len(names))]
# 录入数据
for i, name in enumerate(names):
    print(f'请输入{name}的成绩:')
    for j, course in enumerate(courses):
        # scores[i][j] = float(input(f'{course}:'))
        scores[i][j] = float(60)
print()
print('-' * 5, '学生的平均成绩', '-' * 5)
# 计算每个人的平均成绩
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为:{avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为:{avg_score:.1f}分')
print("-" * 20)
items = ['Python', 'Java', 'Go', 'Swift']

for index in range(len(items)):
    print(f'{index}: {items[index]}')

for index, item in enumerate(items):
    print(f'{index}: {item}')
print('-' * 10, '设计一个函数返回指定日期是这一年的第几天', '-' * 10)


def is_leap_year(year):
    """判断指定的年份是不是闰年，平年返回False，闰年返回True"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """计算传入的日期是这一年的第几天
       :param year: 年
       :param month: 月
       :param date: 日
       """
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    # 布尔值False和True可以转换成整数0和1，因此
    # 平年会选中嵌套列表中的第一个列表(2月是28天)
    # 闰年会选中嵌套列表中的第二个列表(2月是29天)
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date


print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2020, 12, 14))
print('-' * 10, '实现双色球随机选号', '-' * 10)
from random import randint, sample


def display(balls):
    """输出列表中的双色球号码"""
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:0>2d}', end=' ')
    print()


def random_select():
    """随机选择一组号码"""
    # 用生成式生成1到33号的红色球
    red_balls = [x for x in range(1, 34)]
    # 通过无放回随机抽样的方式选中6个红色球
    selected_balls = sample(red_balls, 6)
    # 对红色球进行排序
    selected_balls.sort()
    # 用1到16的随机数表示选中的蓝色球并追加到列表中
    selected_balls.append(randint(1, 16))
    return selected_balls


n = int(input('机选几注:'))
print(n, '注')
for _ in range(n):
    display(random_select())
print('-' * 10, '幸运的女人', '-' * 10)
# 约瑟夫环问题
persons = [True] * 30
persons2 = [x for x in range(1, 31)]
for p in persons2:
    print(p%30)
# counter - 扔到海里的人数
# index - 访问列表的索引
# number - 报数的数字
counter, index, number = 0, 0, 0
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    index %= 30
for person in persons:
    print('女' if person else '男', end='')
