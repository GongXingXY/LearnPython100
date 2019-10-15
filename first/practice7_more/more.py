# 单语句块
flag = True
if flag: print('yes')

# Lambda表格
points = [{'x':2, 'y':3},
          {'x':4, 'y':1}]
points.sort(key=lambda  i: i['y'])
print(points)

'''
要注意到一个 list 的 sort 方法可以获得一个 key 参数，
用以决定列表的排序方式（通常我们只知道升序与降序）。在我们的案例中，我们希望进行一次自定义排序，
为此我们需要编写一个函数，
但是又不是为函数编写一个独立的 def 块，
只在这一个地方使用，
因此我们使用 Lambda 表达式来创建一个新函数。


'''
