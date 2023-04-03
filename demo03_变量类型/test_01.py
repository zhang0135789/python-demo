#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
'''


counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)


'''
多个变量赋值
'''
a = b = c = 1
print (a, b, c)
a, b, c = 1, 2, "runoob"
print (a, b, c)

#标准数据类型
'''
Python3 中常见的数据类型有：
        Number（数字）
        String（字符串）
        bool（布尔类型）
        List（列表）
        Tuple（元组）
        Set（集合）
        Dictionary（字典）

Python3 的六个标准数据类型中：
        不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
        可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''

print("#Number(数字)")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

'''
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
'''
a = 111
print(isinstance(a, int))

'''
注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
'''
print(issubclass(bool, int))
print("True == 1 :", True == 1)
print("False == 0 : ", False == 0)
print("False + 1 :", False + 1)
print("0 is False :", 0 is False)

print("#数值运算")
print("5 + 4 = ", 5 + 4)
print("4.3 - 2 = ", 4.3 - 2)
print("3 * 7 = ", 3 * 7)
print("2 / 4 = ", 2 / 4)
print("2 // 4 = ", 2 // 4)
print("17 % 3 = ", 17 % 3)
print("2 ** 5 = ", 2 ** 5)
'''
注意：
    1、Python可以同时为多个变量赋值，如a, b = 1, 2。
    2、一个变量可以通过赋值指向不同类型的对象。
    3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
    4、在混合计算时，Python会把整型转换成为浮点数。
'''

print("#String（字符串）")
str1 = 'Runoob'
# str = '012345'      #
print (str1)          # 输出字符串
print (str1[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str1[0])       # 输出字符串第一个字符
print (str1[2:5])     # 输出从第三个开始到第五个的字符
print (str1[0:5])
print (str1[2:])      # 输出从第三个开始的后的所有字符
print (str1 * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str1 + "TEST") # 连接字符串

print('Ru\noob')
print(r'Ru\noob')

'''
注意：
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''

print("#bool（布尔类型）")
a = True
b = False

# 比较运算符
print(2 < 3)   # True
print(2 == 3)  # False

# 逻辑运算符
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# 类型转换
print(int(a))   # 1
print(float(b)) # 0.0
print(str(a))   # "True"


print("#List（列表）")

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)

    return output
if __name__ == "__main__":
    input = 'I like runoob 222'
    rw = reverseWords(input)
    print(rw)

print("# Tuple(元组)")
'''
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
'''
注意：
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。
'''














