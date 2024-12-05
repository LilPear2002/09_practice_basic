
def makes10(a, b):
    if a == 10 or b == 10 or a+b == 10:
        return True
    return False

#输入数据
a, b = eval(input())
#调用函数打印结果
print(makes10(a, b))