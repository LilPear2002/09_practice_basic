
def not_string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not' + str

#输入数据
str = eval(input())
#调用函数打印结果
print(not_string(str))