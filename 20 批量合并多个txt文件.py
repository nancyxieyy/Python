# Python读取文件的两个方法
# 方法1: 按行读取
# for line in fin
#
# 方法2: 一次性读取所有内容到一个字符串
# content = fin.read()
import os

data_dir = "20 many_texts"

content = []

# listdir扫描文件夹
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    # 如果是普通文件，且file的结尾是txt格式的，则合并
    if os.path.isfile(file_path) and file.endswith(".txt"):
        # 进行文件读取，直接读取所有文件，然后房屋contents
        with open(file_path) as fin:
            content.append(fin.read())

# 用join形成一个大的字符串
final_content = "\n".join(content)

# 写出成为新的文件
with open("20 many_texts/many_txts.txt", "w") as fout:
    fout.write(final_content)