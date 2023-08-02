# _*_ coding : utf-8 _*_
# @Time : 2023/8/3  03:07
# @Author : nancy_xieyy@icloud.com
# @File : 10 文件的打开与关闭
# @Project : Python

# 使用open函数可以打开一个已经存在的函数，或者创建一个新的文件
# open(文件的路径， 模式)
# w 可写
# r 可读
# 创建一个test.txt文件
# open('test.txt', 'w')

fp = open('test.txt', 'w')
fp.write('hello world')

# 文件的关闭
fp.close()