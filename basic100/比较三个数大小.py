import math

def fun(a,b,c):
    if(a > b):
        if(a > c):
            if(b > c):
                print(a,b,c)
            else:
                print(a,c,b)
        if(a < c):
            print(c,a,b)
    else:
        if(b > c):
            if(a > c):
                print(b,a,c)
            else:
                print(b,c,a)
        else:
            print(c,b,a)
            
def fun2(a,b,c):
    list = [a,b,c]
    list.sort()
    print(f"{list[0]} {list[1]} {list[2]}")
            

fun(2,3,1)
fun(4,7,9)
fun2(8,9,3)
