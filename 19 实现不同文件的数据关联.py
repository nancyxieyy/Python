course_teacher_map = {}
with open("19 course_teacher.txt") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_map[course] = teacher

with open("19 course_student_grade_input.txt") as fin:
    for line in fin:
        line = line[:-1]
        # 获得科目
        course, sno, sname, sgrade = line.split(",")
        # 通过对应科目放置对应老师的名字
        teacher = course_teacher_map.get(course)
        print(course, teacher, sno, sname, sgrade)