
def check(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False