def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

# return 语句用于从函数中返回，也就是中断函数。我们也可以选择在中断函数时从函数中返
# 回一个值。

def some_function():
    pass
# Python 中的 pass 语句用于指示一个没有内容的语句块。
'''
Result:
3
'''