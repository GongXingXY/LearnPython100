import time
num = 20
for i in range(num):
    print('#', end='',flush=True)
    time.sleep(0.5)

days = 365
for i in range(days):
    print("\r","进度百分比:{0}%".format(round((i + 1 ) * 100 / days)),end='', flush=True)
    time.sleep(0.02)
    