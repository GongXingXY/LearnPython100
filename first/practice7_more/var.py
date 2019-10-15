# 传递元组

def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()
print(errnum, errstr)

a = 5; b = 8
# python 中交换两个变量的最快方法是：
a, b = b, a

print(a, b)
# a = 8  b = 5