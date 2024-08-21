import datetime

start_date = "2021-04-28"

end_date = "2021-05-03"

def get_date_range(start_date, end_date):
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        days1_timedelta = datetime.timedelta(days=1)
        start_date = (start_date_obj + days1_timedelta).strftime("%Y-%m-%d")

    return date_list

print(get_date_range(start_date, end_date))