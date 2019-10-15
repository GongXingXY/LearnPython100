import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Loggin to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'

)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
'''
我们使用了三款标准库中的模块——os 模块用以和操作系统交互，platform 模块用以获取平台——操作系统——的信息，logging 模块用来记录（Log）信息。
首先，我们通过检查 platform.platform() 返回的字符串来确认我们正在使用的操作系统（有关更多信息，请参阅import platform; help(platform)）。如果它是 Windows，我们将找出其主驱动器（Home Drive），主文件夹（Home Folder）以及我们希望存储信息的文件名。将这三个部分汇聚到一起，我们得到了有关文件的全部位置信息。对于其它平台而言，我们需要知道的只是用户的主文件夹位置，这样我们就可获得文件的全部位置信息。

我们使用 os.path.join() 函数来将这三部分位置信息聚合到一起。使用这一特殊函数，而非仅仅将这几段字符串拼凑在一起的原因是这个函数会确保完整的位置路径符合当前操作系统的预期格式。
然后我们配置 logging 模块，让它以特定的格式将所有信息写入我们指定的文件。
最后，无论这些信息是用以调试，提醒，警告甚至是其它关键的消息，我们都可以将其聚合并记录。一旦程序开始运行，我们可以检查这一文件，从而我们便能知道程序运行过程中究竟发生了什么，哪怕在用户运行时什么信息都没有显示。
'''