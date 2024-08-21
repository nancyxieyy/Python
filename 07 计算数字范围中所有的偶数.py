# 输入开始和结束值（不包含），得到所有偶数

def get_even(begin, end):
    for i in range(begin, end):
        if i % 2 == 0:
            print(i, " is even number")

get_even(4, 15)

######

def get_even_numbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result

print(get_even_numbers(4, 15))