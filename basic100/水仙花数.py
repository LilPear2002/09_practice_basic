
def judge(num):
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100
    if(ge**3 + shi**3 + bai**3 == num):
        return True
    else:
        return False

def count():
    for i in range(100,1000):
        if(judge(i)):
            print(i)
            
count()
