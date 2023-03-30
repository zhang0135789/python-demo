#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 等待用户输入
# 注：  python2中的raw_input方法在python3中被弃用，用input方法替代

input("按下 enter 键退出，其他任意键显示...\n")


# 同一行显示多条语句
'''
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
'''

import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# print 输出
'''
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,。
# 注：  python2在print的时候不需要(), 但是在python3中需要()
'''
x="a"
y="b"
# 换行输出
print(x)
print(y)

print ('---------')
# 不换行输出
print (x),
print (y),

# 不换行输出
print (x,y)


# 多个语句构成代码组
'''
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。

if expression :
    suite
elif expression :
    suite
else :
    suite 
'''

# 命令行参数
'''
python -h
'''





