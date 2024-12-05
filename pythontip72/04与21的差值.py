
def diff21(n):
    if n < 21:
        return abs(n - 21)
    return (n - 21) * 2

#输入数据
n = eval(input())
#调用函数打印结果
print(diff21(n))