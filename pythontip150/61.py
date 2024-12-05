
def fun(list1,list2):
    list3 = []
    for num in list1:
        if num in list2:
            list3.append(num)
    list3.sort()
    return list3