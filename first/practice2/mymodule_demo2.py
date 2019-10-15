from mymodule import say_hi, __version__

say_hi()
print('Version is', __version__)

'''
你还可以使用：
from mymodule import *
这将导入诸如 say_hi 等所有公共名称，但不会导入 __version__ 名称，因为后者以双下划线开头。

我们大都推荐最好去使用 import 语句，
import mymodule
尽管这会使你的程序变得稍微长一些。

Python 之禅
Python 的一大指导原则是“明了胜过晦涩”2。你可以通过在 Python 中运行 import this 来了解更多内容。
'''

