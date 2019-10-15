'''
数据结构（Data Structures）基本上人如其名——它们只是一种结构，能够将一些数据聚合在一起。换句话说，它们是用来存储一系列相关数据的集合。
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。我们将了解如何使用它们，并利用它们将我们的编程之路变得更加简单。
列表
列表 是一种用于保存一系列有序项目的集合，也就是说，你可以利用列表保存一串项目的序列。想象起来也不难，你可以想象你有一张购物清单，上面列出了需要购买的商品，除开在购物清单上你可能为每件物品都单独列一行，在 Python 中你需要在它们之间多加上一个逗号。
项目的列表应该用方括号括起来，这样 Python 才能理解到你正在指定一张列表。一旦你创建了一张列表，你可以添加、移除或搜索列表中的项目。既然我们可以添加或删除项目，我们会说列表是一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的。
'''

shoplist = ['apple', 'mango', 'banana', 'carrot']
print('I have', len(shoplist), 'Items to purchase.')
print('the Items are:', end='')
for items in shoplist:
    print(items, end=' ')  # 输出列表中全部元素
print('\nI also buy some rice')
shoplist.append('rice')   # 往列表最后添加元素
print('my shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()  # 重新排列列表
print('Sorted shopping list is', shoplist)

print('The first item I will buy is ', shoplist[0]) # 获取列表第一个元素
olditem = shoplist[0]  # 把列表第一个元素赋值给olditem
del shoplist[0]  # 删除列表第一个元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)


