#!/usr/bin/env python3
# 循环语句
'''
Python 中的循环语句有 for 和 while。
'''
print('while 循环')
'''
while 判断条件(condition)：
    执行语句(statements)……
'''
print('使用了 while 来计算 1 到 100 的总和:')
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

print('设置条件表达式永远不为 false 来实现无限循环:')
'''
var = 1
while var == 1 :  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print ("你输入的数字是: ", num)
print ("Good bye!")
'''

'''
while 循环使用 else 语句
    如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''
print('循环输出数字，并判断大小:')
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")

'''
for 语句
    Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
print('用for打印数组：')
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

print('用for打印字符串中的字符：')
word = 'runoob'
for letter in word:
    print(letter)

print('1 到 5 的所有数字：')
for number in range(1, 6):
    print(number)

'''
for...else
    在 Python 中，for...else 语句用于在循环结束后执行一段代码。
    
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码

注意：
    当循环执行完毕（即遍历完 iterable 中的所有元素）后，会执行 else 子句中的代码，如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句。
'''
print('0到6的所有数字：')
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print('以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体，不会执行 else 子句：')
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")






