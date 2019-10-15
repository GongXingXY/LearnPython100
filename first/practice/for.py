for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

# 。在默认情况
# 下， range 将会以 1 逐步递增。如果我们向 range 提供第三个数字，则这个数字将成为逐
# 步递增的加数。同样举个例子来说明， range(1,5,2) 将会输出 [1, 3] 。要记住这一序列扩
# 展直到第二个数字，也就是说，它不会包括第二个数字在内。
# eg 输出100以内的奇数
for k in range(1, 100, 2):
    print(k, end=' ')
'''
Result:
1
2
3
4
The for loop is over
'''
