'''

活在当下的程序员应该都听过"面向对象编程"一词，也经常有人问能不能用一句话解释下什么是"面向对象编程"，我们先来看看比较正式的说法。

"把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。"

这样一说是不是更不明白了。所以我们还是看看更通俗易懂的说法，下面这段内容来自于知乎。
'''
# 面向对象思想有三大要素：封装、继承和多态
'''
定义类
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
'''

class Student(object):
    # __init__是一个特殊方法，用于在创建对时时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self,course_name):
        print('%s 正在学习%s.' % (self.name, course_name))
        # PEP 8 要求标识符的名字用全小写多个单词用下划线连接
        # 但是部分程序员和公司更倾向于使用驼峰命名法
    def watch_move(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》.' % self.name)
        else:
            print('%s 正在观看岛国爱情大电影' % self.name)


