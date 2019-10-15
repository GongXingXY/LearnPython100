def print_max(x, y):
    ''' Prints the maximum of two numbers. 打印两个数值中的最大值

    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    elif x == y:
        print('x y iz equal')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(max(3, 6)) # 内置的对比大小函数
print(print_max.__doc__)
help(print_max)

'''
过一个函数来获取文档
Result:
5 is maximum
 Prints the maximum of two numbers. 打印两个数值中的最大值

    The two values must be integers.这两个数都应该是整数
Help on function print_max in module __main__:

print_max(x, y)
    Prints the maximum of two numbers. 打印两个数值中的最大值
    
    The two values must be integers.这两个数都应该是整数

'''