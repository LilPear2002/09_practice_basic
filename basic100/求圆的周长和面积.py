
def fun1(r):
    return 2 * 3.14 * r

def fun2(r):
    return 3.14 * r**2

r = float(input("请输入半径："))
print("周长为：%.2f" % fun1(r))
print("面积为：%.2f" % fun2(r))