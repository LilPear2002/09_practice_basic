
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

#输入数据
str = eval(input())
#调用函数打印结果
print(string_splosion(str))