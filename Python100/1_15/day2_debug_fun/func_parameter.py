# 函数的参数 function parameter
'''
函数的参数
函数是绝大多数编程语言中都支持的一个代码的"构建块"，
但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，
其中一个显著的区别就是Python对函数参数的处理。
在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，
因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。
'''
from random import randint

def rool_dice(n = 2):
    '''摇色子'''
    total = 0
    for _ in range(n):  # 如果循环中没有用到i 用 _代替
        total += randint(1, 6)
    return total

def add(a = 0, b = 0, c =0):
    ''' 三个数相加'''
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子
print(rool_dice())
# 摇三颗色子
print(rool_dice(3))

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a =100, b=200))


# 其实上面的add函数还有更好的实现方案，
# 因为我们可能会对0个或多个参数进行加法运算，
# 而具体有多少个参数是由调用者来决定，
# 我们作为函数的设计者对这一点是一无所知的，
# 因此在不确定参数个数的时候，我们可以使用可变参数，
# 代码如下所示。

# 在参数名前面的*表示args 是一个可变参数

def add2(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add2())
print(add2(1))
print(add2(1, 2, 3))
print(add2(1, 3, 5, 7, 9))


# Practice1 实现计算求最大公约数和最小公倍数的函数

def gcd(x, y):
    '''求最大公约数'''
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    '''求最小公倍数'''
    return x * y // gcd (x, y)

# Practice2 实现判断一个数是不是回文数的函数

def is_palindrome(num):
    '''判断一个数是不是回文数'''
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


# Practice3 实现判断一个数是不是素数的函数
    
    
def is_prime(num):
    # Practice3 实现判断一个数是不是素数的函数
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

# Practice4 写一个程序判断输入的正整数是不是回文素数
if __name__ == '__main__':
    num = int(input('请输入正整数:'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)

# 全局变量 Global
'''
在实际开发中，我们应该尽量减少对全局变量的使用，
因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，
除此之外全局变量比局部变量拥有更长的生命周期，
可能导致对象占用的内存长时间无法被垃圾回收。
事实上，减少对全局变量的使用，也是降低代码之间耦合度的一个重要举措，
同时也是对迪米特法则的践行。减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，但是如果我们希望将一个局部变量的生命周期延长，使其在定义它的函数调用结束后依然可以使用它的值
，这时候就需要使用闭包，这个我们在后续的内容中进行讲解。
'''
