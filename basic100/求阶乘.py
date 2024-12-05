
# 递归
def fun(num):
    if num == 1:
        return 1
    return num * fun(num - 1)

# 非递归
def fun2(num):
    result = 1
    for i in range(1,num + 1):
        result *= i
    return result

num = int(input("请输入一个整数："))
print(fun(num))
print(fun2(num))