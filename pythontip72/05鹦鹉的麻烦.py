
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

#输入数据
talking, hour = eval(input())
#调用函数打印结果
print(parrot_trouble(talking, hour))