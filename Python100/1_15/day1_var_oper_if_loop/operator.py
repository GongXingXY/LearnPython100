'''
运算符	描述
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= `	= ^= >>= <<=`

'''
# 说明： 在实际开发中，如果搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序。
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag0 and flag1
flag4 = flag1 or flag2 
flag5 = not (1 != 2)

print('flag0 = ', flag0)
print('flag1 = ', flag1)
print('flag2 = ', flag2)
print('flag3 = ', flag3)
print('flag4 = ', flag4)
print('flag5 = ', flag5)
print(flag1 is True)
print(flag2 is not False)

# Practice1 华氏度转换为摄氏度
F = float(input('Plase Enter f'))
c = (F - 32)/1.8
print('%.1f华氏度 = %.1f 摄氏度' % (F, c))
print('{}华氏度 = {}摄氏度'.format(F, c))

# Practice2 输入圆的半径计算周长和面积

import math

radius = float(input('请输入圆的半径'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('该圆的周长为:%.2f' % perimeter)
print('该圆的面积为:%.2f' % area)

# Practice3 输入年份判断是不是闰年

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 !=0) or \
    year % 400 == 0
if is_leap:
    print('是闰年')
else:
    print('不是闰年')

