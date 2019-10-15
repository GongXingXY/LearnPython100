'''
一个模块可以被其它程序导入并运用其功能。我们在使用 Python 标准库的功能时也同样如此。
首先，我们要了解如何使用标准库模块。
'''
import os
import sys
from math import sqrt

print("Square root of 16 is", sqrt(16))
print(os.getcwd())
print('The command line arguments arg:')
for i in sys.argv:
    print(i)


print('\n\nThe PYTHONPATH is', sys.path, '\n')

# from..import 语句
# 如果你希望直接将 argv 变量导入你的程序（为了避免每次都要输入 sys.），那么你可以通过使用 from sys import argv 语句来实现这一点。
#
# 警告：一般来说，你应该尽量避免使用 from...import 语句，而去使用 import 语句。这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。

'''
首先，我们通过 import 语句导入 sys 模块。基本上，这句代码将转化为我们告诉 Python 我们希望使用这一模块。sys 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的系统功能（system）。

当 Python 运行 import sys 这一语句时，它会开始寻找 sys 模块。在这一案例中，由于其是一个内置模块，因此 Python 知道应该在哪里找到它
'''
