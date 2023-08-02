# _*_ coding : utf-8 _*_
# @Time : 2023/8/3  02:03
# @Author : nancy_xieyy@icloud.com
# @File : 09 字符串高级
# @Project : Python

# 获取长度 len
s = 'china'
print(len(s))

# 查找指定内容 find
# 返回某字符在字符串中第一次出现的位置
print(s.find('c'))

# 判断
print(s.startswith('c'))
print(s.endswith('a'))

# count
print(s.count('a'))

# 替换
print(s.replace('c', 'd'))

# 切割
s1 = '1#2#3'
print(s1.split('#'))

# 转大写
print(s.upper())
# 转小写
print(s.lower())

# 去除空格
s2 = '      a       '
print(len(s2.strip()))