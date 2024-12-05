
def front3(str):
    if len(str) <= 3:
        return str * 3
    return str[0:3] * 3

#输入数据
str = eval(input())
#调用函数打印结果
print(front3(str))