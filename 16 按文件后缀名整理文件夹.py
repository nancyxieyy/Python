import os
import shutil

dir = "/Users/nancyxie/Desktop/Coding/Python/Python基础"

for file in os.listdir(dir):
    # splitext得到文件的后缀
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    # 判断该目录下有没有该后缀的文件夹，没有则创造
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    # 移动文件
    shutil.move(source_path, target_path)
