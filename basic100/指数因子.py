
# 输入一个正整数，输出其所有质数因子

a = int(input('请输入一个正整数：'))
y = 2
list = []

while a != y:
    if a % y == 0:
        list.append(y)
        a = a / y
    else:
        y += 1
        
list.append(int(a))
for i in list:
    print(i,end=' ')
