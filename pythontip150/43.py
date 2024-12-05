import datetime

def calculate_days_between(date1, date2):
    # 字符串转换为datetime对象，并计算date2和date1之间的差异，以天为单位
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    difference = date2 - date1
    return difference.days