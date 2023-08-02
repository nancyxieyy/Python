# _*_ coding : utf-8 _*_
# @Time : 2023/8/2  01:01
# @Author : nancy_xieyy@icloud.com
# @File : 07 程序控制语句
# @Project : Python

# 在控制台上输入您的成绩分数
# 如果90以上 成绩优秀
# 如果80以上 成绩良好
# 如果70以上 成绩中等
# 如果60以上 成绩合格
# 否则 成绩不合格
score = int(input('请输入您的成绩'))
if score >= 90:
    print('您的成绩优秀')
elif score >= 80:
    print('您的成绩良好')
elif score >= 70:
    print('您的成绩中等')
elif score >= 60:
    print('您的成绩合格')
else:
    print('您的成绩不合格')