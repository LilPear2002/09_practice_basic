
def last2(str):
    if len(str) <= 2:
        return 0
    last2_str = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i+2] == last2_str:
            count += 1
    return count


#输入数据
str = eval(input())
#调用函数打印结果
print(last2(str))