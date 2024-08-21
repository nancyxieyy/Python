# 学生成绩数据格式：
# 复杂列表，元素是字典或者元组
# [{'sno': 101, 'sname':"小张", 'sgrade':88}
# {'sno': 102, 'sname':"小王", 'sgrade':77}
# {'sno': 103, 'sname':"小李", 'sgrade':99}
# {'sno': 104, 'sname':"小赵", 'sgrade':66}]
#

students = [{'sno': 101, 'sname':"小张", 'sgrade':88},
        {'sno': 102, 'sname':"小王", 'sgrade':77},
        {'sno': 103, 'sname':"小李", 'sgrade':99},
        {'sno': 104, 'sname':"小赵", 'sgrade':66}]

# key处写一个函数表示根据成绩排序（降序）
students_sort = sorted(students, key=lambda x:x["sgrade"], reverse=True)

print(f"source: {students}")
print(f"sort result: {students_sort}")