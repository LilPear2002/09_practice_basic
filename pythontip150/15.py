
def fun(string):
    my_dict = {}
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    count = 0
    for key in my_dict.keys():
        count += 1
    return count == 1
