
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

#输入数据
a, b = eval(input())
#调用函数打印结果
print(sum_double(a, b))