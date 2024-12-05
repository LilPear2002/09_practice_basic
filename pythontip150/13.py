
def fun(num):
    num_str = str(num)
    my_list = list(num_str[::-1])
    num_list = []
    for i in my_list:
        num_list.append(int(i))
    return num_list