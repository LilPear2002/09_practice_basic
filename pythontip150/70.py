
def fun(lst):
    count_dict = {}
    for str in lst:
        if str in count_dict:
            count_dict[str] += 1
        else:
            count_dict[str] = 1
    return count_dict