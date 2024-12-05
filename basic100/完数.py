
# 一个数恰好等于除了它以外所有数的和，这个数就称为“完数”。例如6，28，496等。求1000以内所有的完数

def judge(num):
    sum = 0
    for i in range(1,num):
        if(num % i == 0):
            sum += i
    return num == sum

def count():
    for i in range(1,1001):
        if(judge(i)):
            print(i,end=' ')
            
count()