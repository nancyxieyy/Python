import datetime

def get_diff_days(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return  pdate_result.strftime("%Y-%m-%d")

print(get_diff_days("2014-8-21", 1))
print(get_diff_days("2014-8-21", 3))
print(get_diff_days("2014-8-21", 5))
print(get_diff_days("2014-8-21", 7))