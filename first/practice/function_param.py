def print_max(a, b):  # 这里的参数称为形参
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to ', b)
    else:
        print(b, 'is maximum')

print_max(3, 4)  # 这里的参数称为实参

x = 5
y = 7
print_max(x, y)
'''
Result:
4 is maximum
7 is maximum
'''