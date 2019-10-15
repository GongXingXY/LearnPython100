import os
import time
 
# 需要备份的文件指定在一个目录中。

source = ['E:\\test']  # 定义一个列表路径 source

# 备份文件必须存储在一个主备份目录中

target_dir = 'F:\\Backup'  # 定义一个元组路径 target_dir

# 如果目标目录还不存在，则进行创建

if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

today = target_dir + os.sep + time.strftime('%Y%m%d')  # 创建目录并以当前年月日命名

now = time.strftime('%H%M%S')  # 获取时分秒

# 添加一条来自用户的注释以创建
# zip 文件的文件名
comment = input('Enter a comment --> ')

# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ','_') + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

# 我们使用zip 命令将文件打包成zip格式 
zip_command = "zip -r {0} {1}".format(target,' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


'''
软件开发流程
1、What 做什么  （分析）
2、HOW  怎么做  （设计）
3、Do it 开始做 （执行）
4、TEST  测试   （测试与修复错误）
5、USE   使用   （操作或开发）
6、Maintain 维护 （改进）

程序是成长起来的，不是搭建起来的


'''