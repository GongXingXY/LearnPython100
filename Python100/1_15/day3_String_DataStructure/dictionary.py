'''
字典是另一种可变容器模型,类似于我们生活中使用的字典,它可以存储
任意类型对象,与列表,集合不同的是,字典的每个元素都是由一个键
和一个值组成的'键值对',健和值通过冒号分开.下面的代码演示了如何定义和
使用字典

'''

scores = {'骆昊':95, '沙发椅':78, '李白 ':82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['沙发椅'])
#　对字典进行遍历(遍历的其实是键再通过键取的值)
for elem in scores:
    print('%s\t --> \t%d' % (elem, scores[elem]))

# 更新字典中的元素
scores['少数人'] = 65
scores['诸葛王良'] = 71
scores.update(冷面=67, 方 = 85)
print(scores)

if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法 也是通过键获取对应的值,但是可以设置默认值 
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)

