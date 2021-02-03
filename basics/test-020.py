# coding=utf-8
print('*' * 20, '函数使用进阶', '*' * 20)
print('-' * 10, '关键字参数', '-' * 10)


def can_form_triangle(a, b, c):
    print(f'a={a},b={b},c={c}')
    return a + b > c and b + c > a and a + c > b


# 调用函数传入参数不指定参数名按位置对号入座
print(can_form_triangle(1, 2, 3))
# 调用函数通过“参数名=参数值”的形式按顺序传入参数
print(can_form_triangle(a=1, b=2, c=3))
# 调用函数通过“参数名=参数值”的形式不按顺序传入参数
print(can_form_triangle(c=3, a=1, b=2))


# 命名关键字参数取代位置参数,*前面的参数都是位置参数，而*后面的参数就是命名关键字参数
def can_form_triangle2(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# print(is_valid_for_triangle2(3, 4, 5))
# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_form_triangle2(a=3, b=4, c=5))
print(can_form_triangle2(c=5, b=4, a=3))


# *args并不能处理带参数名的参数
def calc(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# TypeError: calc() got an unexpected keyword argument 'a'
# print(calc(a=1,b=2,c=3))
# 既不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名,同时使用可变参数和关键字参数
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc())  # 0
print(calc(1, 2, 3))  # 6
print(calc(a=1, b=2, c=3))  # 6
# 不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前
print(calc(1, 2, c=3, d=4))  # 10
print('-' * 10, '高阶函数的用法', '-' * 10)

import operator


def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


# 调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))  # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))  # 120
# 顺序要对
print(calc(1, 2, 3, x=4, y=5, init_value=0, op=operator.add))  # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=operator.mul))  # 120


# 不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，否则将会引发异常。
# 例如，执行calc(1, 2, c=3, d=4, 5)将会引发SyntaxError错误，
# 错误消息为positional argument follows keyword argument，
# 翻译成中文意思是“位置参数出现在关键字参数之后”。
# 1,2,3必须在第一位，因为前面都是带参数命名的参数
# print(calc(init_value=0, op=operator.add, 1, 2, 3, x=4, y=5))      # 15
# print(calc(init_value=1, op=operator.mul, 1, 2, x=3, y=4, z=5,))    # 120
def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)  # [144, 64, 3600, 2704]
# 列表生成式
numbers3 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers3)  # [144, 64, 3600, 2704]
# lambda函数
numbers4 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers1)))
print(numbers4)  # [144, 64, 3600, 2704]


# *args可变参数,**kwargs关键字参数 init_value=0 命名关键字参数
# 命名关键字参数要放在可变参数和关键字参数之间，传参时先传入可变参数，关键字参数和命名关键字参数的先后顺序并不重要。
def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# 调用calc函数，使用init_value和op的默认值
print(calc(1, 2, 3, x=4, y=5))  # 15
# 调用calc函数，通过lambda函数给op参数赋值
print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))  # 120
import operator, functools

# 一行代码定义求阶乘的函数
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
# 调用Lambda函数
print(fac(10))  # 3628800
print(is_prime(9))  # False
