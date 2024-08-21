# 创建一个放兴趣爱好的字典
like_count = {}

with open("21 student_like.txt") as fin:
    for line in fin:
        line = line[:-1]
        # 用空格拆封姓名和兴趣
        sname, likes = line.split(" ")
        # 用逗号拆封每一个兴趣
        like_list = likes.split(",")
        # 在兴趣列表里，如果某个兴趣不在兴趣字典李，则该兴趣数量为0
        for like in like_list:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1

print(like_count)