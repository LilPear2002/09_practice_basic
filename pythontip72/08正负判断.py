
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)

#输入数据
a, b, negative = eval(input())
#调用函数打印结果
print(pos_neg(a, b, negative))