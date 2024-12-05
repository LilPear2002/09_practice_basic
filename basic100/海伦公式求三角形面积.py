
import math

def fun(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input("输入第一条边: \n"))
b = float(input("输入第二条边: \n"))
c = float(input("输入第三条边: \n"))

s = fun(a,b,c)
print("此三角形面积为{:.2f}".format(s))