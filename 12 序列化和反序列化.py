# _*_ coding : utf-8 _*_
# @Time : 2023/8/3  03:23
# @Author : nancy_xieyy@icloud.com
# @File : 12 序列化和反序列化
# @Project : Python

fp = open('test.txt', 'w')

name = ['zhangsan', 'lisi']

# dumps()
# 导入json模块到文件中
import json

# 将python对象变成了一个json字符串
names = json.dumps(name)

# 将names写入到文件中
fp.write(names)

fp.close()