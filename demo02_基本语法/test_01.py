
#Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：

# python 标识符
'''
# 在 Python 里，标识符由字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
'''

# python 行和缩进
'''
# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
'''

if True:
    print ("Answer")
    print("True")
else:
    print ("Answer")
    print("False")


# Python 多行语句
'''
# Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
'''
# total = item_one + \
#     item_two +\
#     item_three

'''
# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
'''
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须是相同类型的。

print('Hello , python!')
print("""hello, 3 python!""")

# Python空行
'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

'''



