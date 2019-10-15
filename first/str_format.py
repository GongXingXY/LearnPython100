age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))
'''
Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置
'''
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# print 格式不换行， end=''
# 单引号里面可以加字符以分割
print('a', end=' ')
print('b')

# 转义序列  \
print('what\'s you name?')
print('\\')
# \n  表示换行
print('Hi \nMy name is xxx')
# \t 制表符
print('test \t test')
# \ 字符串末尾有一个\ 代表继续
print('This is the first sentence.\
This is the second sentence')
# r  代表原始字符，即是不转义
print(r'\\n\t')

#  变量命名规则
# 第一个字符必须是字母或者_
# 区分大小写

# 对象 ，Python 将程序中的任何内容统称为 对象（Object）
# Python 是强（Strongly）面向对象的，因为所有的一切都是对象， 包括数字、字符串与函数。

# 运算与表达式
# 精确除法 /， 整除 //
# 数值运算与赋值的快捷方式
a = 2
a = a + 3  # 5
a += 3  # 8
print(a)

# 控制流 主要有三种 if for while

