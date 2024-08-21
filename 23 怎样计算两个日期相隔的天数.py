import datetime

birthday = "2002-07-09"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")

curr_datetime = datetime.datetime.now()

# Python可以直接相减获得
minus_datetime = curr_datetime - birthday_date
print(minus_datetime.days)
print(minus_datetime.days/365)