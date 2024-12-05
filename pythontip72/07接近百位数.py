
def near_hundred(n):
    if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
        return True
    return False

#输入数据
n = eval(input())
#调用函数打印结果
print(near_hundred(n))