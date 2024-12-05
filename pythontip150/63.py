
def fun(lst):
    lst.sort()
    differ = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] > differ:
            differ = lst[i] - lst[i - 1]
    return differ