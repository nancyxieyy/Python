# _*_ coding : utf-8 _*_
# @Time : 2023/8/1  18:25
# @Author : nancy_xieyy@icloud.com
# @File : 05 类型转换
# @Project : Python

# str -> int
a = '123'
print(type(a))
b = int(a)
print(type(b))

# float -> int
c = 1.55
print(type(c))
d = int(c)
# 会返回小数前面的数字
print(type(d))

# boolean -> int
e = True
print(type(e))
f = int(e)
# 会返回小数前面的数字
print(type(f))


aa = '12.34'
print(type(aa))
bb = float(aa)
print(bb)
print((type(bb)))