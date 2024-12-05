def monkey_trouble(a_smile, b_smile):
    if((a_smile == True and b_smile == True) or (a_smile == False and b_smile == False)):
        return True
    else:
        return False

#输入数据
a_smile, b_smile = eval(input())
#调用函数打印结果
print(monkey_trouble(a_smile, b_smile))