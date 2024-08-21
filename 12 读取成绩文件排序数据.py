# 输入文件：
#   三列：学号、姓名、成绩
#   列之间用都好分割，比如“101，小张，88”
#   行之间用\n换行分割
# 处理：
#   读取文件，按成绩倒序排列
# 输出：
#   排序后的三列数据

def read_file():
    result = []
    with open("./12 students_grade_input.txt") as fin:
        for line in fin:
            # 去掉最后一个换行符，保留其他
            line = line[:-1]
            # 逗号分隔
            result.append(line.split((",")))
    return result

def sort_grades(datas):
    # 用成绩来排序，但是要从字符串类型转变成int类型
    return sorted(datas, key=lambda x:int(x[2]), reverse=True)

def write_file(datas):
    with open("./12 students_grade_output.txt", "w") as fout:
        for data in datas:
            # 元素的逗号分隔，
            fout.write(",".join(data) + "\n")

# 读取文件
datas = read_file()

# 排序数据
datas = sort_grades(datas)

# 写出文件
write_file(datas)