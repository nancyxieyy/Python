# _*_ coding : utf-8 _*_
# @Time : 2023/8/3  03:15
# @Author : nancy_xieyy@icloud.com
# @File : 11 文件的读写
# @Project : Python

# 写数据
# write方法
# w时，如果文件存在，会先清空再添加
# a 可以添加
fp = open('test.txt', 'a')

fp.write('world\n'*5)

fp = open('test.txt', 'r')

# read一个个字读取
# readline一行行读取
# readlines会读取并以列表的形式返回
content = fp.readline()
print(content)

fp.close()
