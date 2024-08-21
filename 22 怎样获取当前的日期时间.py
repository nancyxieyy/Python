import datetime

curr_datetime = datetime.datetime.now()

print(curr_datetime, type(curr_datetime))

# 1. 变成字符串
str_time = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(str_time)

# 2. 分别获取某个时间
print("year:", curr_datetime.year)
print("month:", curr_datetime.month)
print("day:", curr_datetime.day)
print("hour:", curr_datetime.hour)
print("minute:", curr_datetime.minute)
print("second:", curr_datetime.second)