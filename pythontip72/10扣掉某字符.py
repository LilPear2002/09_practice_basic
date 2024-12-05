
def missing_char(str, n):
    return str[:n] + str[n+1:]

#输入数据
str, n = eval(input())
#调用函数打印结果
print(missing_char(str, n))