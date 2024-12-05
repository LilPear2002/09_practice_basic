
# 判断一个数是否是素数

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(8))