# 输入开始数字和结束数字，打印区间内的所有素数

def is_prime(number):
    if number in (1, 2):
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_prime(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, " is a prime")

get_prime(11, 25)