
def sort(a,b,c):
    list = [a,b,c]
    list.sort()
    return list

def judge(a,b,c):
    list = sort(a,b,c)
    if(list[0] + list[1] > list[2] and list[2] - list[1] < list[0]):
        return True
    return False
    

try:
    a = float(input("输入第一条边: \n"))
    b = float(input("输入第二条边: \n"))
    c = float(input("输入第三条边: \n"))

    # 验证输入是否为正数
    if a <= 0 or b <= 0 or c <= 0:
        print("边长必须为正数！")
    else:
        print(judge(a, b, c))
except ValueError:
    print("请输入有效的数字！")
