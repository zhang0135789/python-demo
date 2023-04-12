#!/usr/bin/python3

# Python3 条件控制
'''
Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。

注意：
    1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能也类似
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''

var1 = 100
if var1:
    print('1 - if 表达式条件为true')
    print(var1)

var2 = 0
if var2:
    print('2 - if 表达式条件为true')
    print(var2)
else:
    print('2 - if 表达式为false')

print("--------------------------------------------")
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

print("--------------------------------------------")
'''
if 嵌套
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


'''
if 嵌套
    在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
'''

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")

'''
match...case
    Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。
    match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_ 可以匹配一切。
match subject:
case <pattern_1>:
    <action_1>
case <pattern_2>:
    <action_2>
case <pattern_3>:
    <action_3>
case _:
    <action_wildcard>

注意：
    在python3.10 中才能使用
'''
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))
'''



