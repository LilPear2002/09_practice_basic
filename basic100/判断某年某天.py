import datetime
# 输入年月日 判断是一年中的第几天

# 方法一
def count(year,month,day):
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    for i in range(month-1):
        sum += day_list[i]
    sum += day
    if(year%4==0 and year%100!=0 or year%400==0):
        sum += 1
    return sum

# 方法二
def count2(year,month,day):
    yuandan = datetime.date(year,1,1)
    now = datetime.date(year,month,day)
    days = (now-yuandan).days + 1
    return days

year,month,day = map(int,input().split())
print(count(year,month,day))
print(count2(year,month,day))