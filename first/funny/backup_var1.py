import os
import time

# 需要备份的文件指定在一个列表中。

source = ['E:\\test']  # 定义一个列表路径 source

# 备份文件必须存储在一个主备份目录中

target_dir = 'F:\\Backup'  # 定义一个元组路径 target_dir

# 备份文件将打包压缩成zip文件。
# zip压缩文件的文件名由当前日期与时间构成。
# os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔符
target = target_dir + os.sep + \
         time.strftime('%Y-%m-%d %H:%M:%S') + '.zip'

# 如果目标目录还不存在，则进行创建

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 我们使用zip命令将文件打包成zip 格式

zip_command = 'zip -r {0} {1}'.format(target,
                                       ' '.join(source))

# 运行备份

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
