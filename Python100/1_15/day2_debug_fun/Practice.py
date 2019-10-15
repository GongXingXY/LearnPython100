'''
在学习了Python的核心语言元素（变量、类型、运算符、表达式、分支结构、循环结构等）之后，
必须做的一件事情就是尝试用所学知识去解决现实中的问题，
换句话说就是锻炼自己把用人类自然语言描述的算法（解决问题的方法和步骤）
翻译成Python代码的能力，而这件事情必须通过大量的练习才能达成。
'''

#　1 寻找水仙花数 ， 3位数，该数字每个位上数字的立方之和正好等于它本身

for num in range(100, 1000):
    low = num % 10   # 把个位数找出来 eg : 100 = 0 101 =1
    mid = num // 10 % 10  # 把十位数找出 中间的数
    high = num // 100  # 把百位数找出
    if num == low ** 3 + mid ** 3 + high ** 3: # 如果这个数等于每个数立方之和
        print(num)

# 2 正整数的反转

num = int(input('num = '))
resersed_num = 0

while num > 0:
    resersed_num = resersed_num * 10 + num % 10  # 取出最右的一位，
    num //= 10  # 判断是不是最左的一位了，如果是 返回0
print(resersed_num)





# 3 百钱百鸡 问题 公鸡5元一只 ， 母鸡3元一只， 
# 小鸡 1元 三只，100块买一百只鸡，其中各有多少只？

for x in range(1, 20): # 20 * 5 <= 100
    for y in range(1, 33):  # 33 * 3 <=100
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：%d只, 母鸡：%d只，小鸡：%d只' %(x, y, z))
'''
上面使用的方法叫做穷举法，也称为暴力搜索法，
这种方法通过一项一项的列举备选解决方案中所有可能
的候选项并检查每个候选项是否符合问题的描述，
最终得到问题的解。这种方法看起来比较笨拙，
但对于运算能力非常强大的计算机来说，通常都是
一个可行的甚至是不错的选择，而且问题的解如果存在，
这种方法一定能够找到它'''






# 4 CRARS 赌博游戏
'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
# 我们设定玩家开始游戏时有1000元赌注
游戏结束的条件是玩家输光赌注'''

from random import randint

money = 1000 
while money > 0:
    print('你的总资产为：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d 点' % first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        needs_go_on = True
        
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束')



