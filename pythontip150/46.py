
def fun(dictionary):
    my_list = []
    for key, value in dictionary.items():
        my_list.append([key, value])
    my_list.sort()
    return my_list