def sleep_in(weekday, vacation):
    if(weekday == False or vacation == True):
        return True
    else:
        return False

#输入数据
weekday, vacation = eval(input())
#调用函数打印结果
print(sleep_in(weekday, vacation))