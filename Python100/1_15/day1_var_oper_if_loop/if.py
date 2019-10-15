# 分支结构

confirm = True

while confirm:
    username = input('Enter userName: ')
    password = int(input('Enter passWord: '))
    if username == 'admin' and password == 123456:
        print('身份验证通过')
        break
    elif username == 'admin' and password != 123456:
        print('请检查密码')
    else:
        print('请检查账号')


x = float(input('x = '))
if x > 1:
    y = 3 * x -5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


# Practice1 英制单位英寸与公制单位厘米互换

value = float(input('请输入长度： '))
unit = input ('请输入单位： ')
if unit == 'in' or unit == '英寸':
    print('%.1f英寸 = %.1f 厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.1f厘米 = %.1f英寸' % (value, value /2.54))
else:
    print('请输入有效单位')

# Practice2 百分制成绩转换为等级制成绩

score = float(input('Enter your score: '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif  score >= 60:
    print('D')
else:
    print('F')

#Practice3 输入三条边长，如果能构成三角形就计算周长和面积

a = float(input('a = '))
b = float(input('a = '))
c = float(input('c = '))
if a + b > c and a + c > b and b +c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c ) / 2
    area = (p * (p - a) * (p - b) *(p-c)) ** 0.5
    print('面积：%f' % (area))
else:
    print('不能构成三角形')

#说明： 上面使用的通过边长计算三角形面积的公式叫做海伦公式。



   

