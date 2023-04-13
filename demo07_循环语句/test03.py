#!/usr/bin/env python3

'''
break 和 continue 语句及循环中的 else 子句

    break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
    continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''

print('while 中使用 break：')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束')

print('while 中使用 continue：')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

print('更多实例:')
print('第一个实例:')
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)
print('第二个实例:')
var = 10  # 第二个实例
while var > 0:
    print('当前变量值为 :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")

print('循环字符串 Runoob，碰到字母 o 跳过输出：')
for letter in 'Runoob':
    if letter == 'o':
        continue
    print(letter)
print('变量为 5 时跳过输出:')
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print(var)
print("Good bye!")

'''
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
'''
print('寻找质数：')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

'''
pass语句
    Python pass是空语句，是为了保持程序结构的完整性。
    pass 不做任何事情，一般用做占位语句，
'''

print('在字母为 o 时 执行 pass 语句块:')
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)
print("Good bye!")
while True:
    pass  # 等待键盘中断 (Ctrl+C)
    break
print('中断..')
