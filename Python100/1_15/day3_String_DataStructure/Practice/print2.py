def get_suffix(filename, has_dot = False):
    # 获取文件名的后缀名

    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return 'zip'
# 设计一个函数返回传入的列表中最大和第二大的元素的值  
def max2(x):
    m1, m2 = (x[0], x[1] if x[0] > x[1] else (x[1], x[0]))
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1 
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

# 计算指定的年月日是这一年的第几天

def is_leap_year(year):
    '''
    判断指定的年份是不是闰年

    '''
    return year % 4 == 0 and year % 100 != 0 or year % \
        400 ==0
def which_day(year, month, date):

    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ][is_leap_year(year)]
    total = 0 
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980,11,28))
    print(which_day(1981,12,31))
    print(which_day(2018,1,1))
    print(which_day(2016,3,1))

if __name__=='__main__':
    main()



