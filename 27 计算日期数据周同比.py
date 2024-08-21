import datetime

date_sale = {}

is_first_line = True
with open("27 date_sale_data.txt") as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale_number = line.split("\t")
        date_sale[date] = float(sale_number)

def get_diff_days(date, days):
    # 当前日期
    curr_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    timedelta = datetime.timedelta(days=-days)
    return (curr_date + timedelta).strftime("%Y-%m-%d")

for date, sale_number in date_sale.items():
    # 找到7天前的日期
    date7 = get_diff_days(date, 7)
    # 7天前的日前有可能找不到的，则赋值为0
    sale_number7 = date_sale.get(date7, 0)
    if sale_number7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = (sale_number - sale_number7) / sale_number7
        print(date, sale_number, date7, sale_number7, week_diff)