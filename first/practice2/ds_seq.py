shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swroop'

# indexing or 'Subscription' operation #
# 索引或下标 （Subscription）操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 3 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

#  在切片操作中，第一个数字（冒号前面的那位）指的是切片开始的位置，第二个数字（冒号后面的那位）指的是切片结束的位置。
#  如果第一位数字没有指定，Python 将会从序列的起始处开始操作。
#  如果第二个数字留空，Python 将会在序列的末尾结束操作。
#  要注意的是切片操作会在开始处返回 start，并在 end 前面的位置结束工作。
#  也就是说，序列切片将包括起始位置，但不包括结束位置。

