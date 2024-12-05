
def fun(str_list):
    my_list = str_list.split(" ")
    my_dict = {}
    index = 0
    for str in my_list:
        for i in range(len(str)):
            if str[i] == '=':
                index = i
        my_dict[str[0:index]] = str[index+1:]
    return my_dict