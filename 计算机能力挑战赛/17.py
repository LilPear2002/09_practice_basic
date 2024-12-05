
def judge(num):
    num_str = str(num)
    sum = 0
    for i in num_str:
        sum += int(i) ** 2
    return sum > num

def find_num(n,m):
    for i in range(n,m + 1):
        if judge(i):
            print(i)

n,m = map(int,input().split(" "))
find_num(n,m)