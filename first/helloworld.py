def isEqual(num1, num2): # 这是一个自定义函数
    if num1 < num2:
        print('too small')
        return False
    elif num1 > num2:
        print('too big')
        return False
    else:
        print('bingo')
        return True


from random import randint

num = randint(1, 100)
print(list(range(1,10)))
print('Guess what I think?')
bingo = False
while not False != bingo:
    answer = int(input())
    bingo = isEqual(answer, num)
