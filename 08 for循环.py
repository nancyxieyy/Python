# _*_ coding : utf-8 _*_
# @Time : 2023/8/2  01:06
# @Author : nancy_xieyy@icloud.com
# @File : 08 for循环
# @Project : Python

s = 'china'
# s代表要遍历的数据
for i in s:
    print(i)

# range方法的结果 一个可以遍历的对象
for i in range(5):
    print(i)

# range(起始值，结束指)
# 左闭右开
for i in range(1, 5):
    print(i)

# range(起始值，结束指，步长)
# 左闭右开
for i in range(1, 11, 3):
    print(i)