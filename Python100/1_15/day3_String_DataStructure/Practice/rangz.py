import random

def generate_code(code_leng=4):
    #生成指定长度的验证码

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_leng):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
