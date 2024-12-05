
def fun(lst):
    big_num = -1
    for num in lst:
        if num % 2 == 0:
            if num > big_num:
                big_num = num
    return big_num