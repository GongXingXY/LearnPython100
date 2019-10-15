#在Python 中构造循环结构有两种做法，一种是 for - in 一种是while

# for in 循环

# 用for 循环实现1~100求和

sum = 0
for x in range(101):
    sum += x

print(sum)

'''
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
'''
# 计算100中偶数和
sum = 0
for x in range(2,101, 2):
    sum += x
print(sum)

# 用分支结构
sum = 0 
for x in range(1,101):
    if x % 2 == 0:
        sum += x

print(sum)

# 输出乘法口诀表（九九表）
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, i * j),end='\t')
    print()


# while 循环

'''
猜数字游戏
'''
import random

answer = random.randint(1, 100) # 随机生成1-100以内的数字
counter = 0 # 计数
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break
print('你总共猜了%d次 ' % counter)
if counter > 7:
    print('你的智商余额明显不足')

#Practice1 输入一个正整数判断是不是素数

from math import sqrt 

num = int(input('请输入一个正整数： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num !=1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

#Practice2 输入两个正整数，计算它们的最大公约数和最小公约数

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y 就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x，x的值赋给y
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公约数是%d' % (x, y, x*y // factor))
        break
