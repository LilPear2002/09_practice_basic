
def fun(string):
    list1 = string.split("/")
    list2 = []
    list2.append(list1[1])
    list2.append(list1[0])
    list2.append(list1[2])
    str1 = ''.join(list1)
    str2 = ''.join(list2)
    str1_reverse = str1[::-1]
    str2_reverse = str2[::-1]
    if str1 == str1_reverse and str2 == str2_reverse:
        return True
    else:
        return False
