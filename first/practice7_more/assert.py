# assert 断言

mylsit = ['item']
assert len(mylsit) >=1
print(mylsit.pop())
assert len(mylsit) >=1

'''你应该明智地选用 assert 语句。
在大多数情况下，它好过捕获异常，
也好过定位问题或向用户显示错误信息然后退出。'''
