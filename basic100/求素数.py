
# 判断素数
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# 求区间内的素数
def prime_range(x,y):
    list = []
    for i in range(x,y + 1):
        if(is_prime(i)):
            list.append(i)
    return list
    
print(prime_range(1,100))