# 输入文件：
#   三列：学号、姓名、成绩
#   列之间用都好分割，比如“101，小张，88”
#   行之间用\n换行分割
# 输出：
#   最高分、最低分、平均分

def compute_score():
    scores = []
    with open("13 students_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(",")
            # 插入最后一列(成绩)，且转换成int
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores))
    return max_score, min_score, avg_score

def read_file():
    result = []
    with open("13 students_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result

def get_highest_grade(datas):
    datas = sorted(datas, key=lambda x:int(x[2]), reverse=True)
    highest_grade = datas[0][2]
    return highest_grade

def get_lowest_grade(datas):
    datas = sorted(datas, key=lambda x:int(x[2]))
    lowest_grade = datas[0][2]
    return lowest_grade

def get_average_grade(datas):
    number = len(datas)
    sum = 0
    for i in range(number):
        sum += int(datas[i][2])

    return sum/number

# 读取文件
datas = read_file()

# 最高分
print("The highest grade is ", get_highest_grade(datas))

# 最低分
print("The lowest grade is ", get_lowest_grade(datas))

# 平均分
print("The average grade is ", get_average_grade(datas))