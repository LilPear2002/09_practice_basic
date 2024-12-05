# 打印100内的偶数

# 方式一
for i in range(2,101,2):
    print(f"{i}\t",end='')
    
print('\n')

# 方式二
for i in range(1,101):
    if i % 2 == 0:
        print(f"{i}\t",end='')
        
print('\n')

# 方式三
mylist = []
for i in range(1,100):
    if i % 2 != 0:
        mylist.append(i)
print(mylist)
