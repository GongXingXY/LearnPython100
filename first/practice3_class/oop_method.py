class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()
p.say_hi()
# 前面两行可以写作
# Person().say_hi()

'''
self
类方法与普通函数只有一种特定的区别
——前者必须多加一个参数在参数列表开头，
这个名字必须添加到参数列表的开头，
但是你不用在你调用这个功能时为这个参数赋值，
Python 会为它提供。这种特定的变量引用的是对象本身，
按照惯例，它被赋予 self 这一名称。
'''
