
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str)-1]
    return str[-1] + mid + str[0]

#输入数据
str = eval(input())
#调用函数打印结果
print(front_back(str))