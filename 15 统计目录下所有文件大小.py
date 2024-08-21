import os

# 获取单个文件的大小
print(os.path.getsize("14 随便找的文章.txt"))

sum_size = 0
# 列出目录下所有文件
for file in os.listdir("."):
    # 判断是否是文件（因为可能返回一个目录）
    if os.path.isfile(file):
        sum_size += os.path.getsize((file))

print("all size of dir: ", sum_size/1000, "kb")