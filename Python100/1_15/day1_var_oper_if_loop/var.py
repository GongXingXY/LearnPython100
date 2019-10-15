a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# type() 检查变量的类型

a = 100
b = 12.345
c = 1 + 5j
d = 'helloworld'
e = True
def sayhi():
    print('hi')
class Test():
    def hello(self):
        print('hello')

fun = sayhi
cla = Test()

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(fun))
print(type(cla))

# Python内置函数对变量类型进行转换
'''
int() 将一个数值或者字符串转换成整数，可以指定进制
float() 将一个字符串转换成浮点数
str() 将指定对象转换成字符串形式，可以指定编码
chr() 将整数转换成该编码对应的字符串(一个字符)
ord() 将字符串（一个字符）转换成对应的编码（整数）

'''

test = 10
teststr = str(test)
print(teststr + 'e')
print(type(teststr))


number1 = int(input('number1 = '))
number2 = int(input('number2 = '))
# 两种方式
print('%d + %d = %d' % (number1, number2, number1 + number2)) # 占位符语法 
print('{0} + {1} = {2}'.format(number1,number2, number1+number2))  # format 语法
