# 求数字的阶乘
# 6的阶乘： 6*5*4*3*2*1

num = 6
res = 1
for i in range(1, num+1):
    res *= i

print("6! = ", res)

####
def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

print("jiecheng 6 = ", get_jiecheng(6))