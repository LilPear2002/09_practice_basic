
def fun(lst):
    num_dict = {}
    for num in lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    my_list = []
    for key,value in num_dict.items():
        if value == 1:
            my_list.append(key)
    return my_list