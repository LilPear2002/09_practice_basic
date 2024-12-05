
def fun(input_string):
    count_dict = {}
    for char in input_string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    count = 0
    for value in count_dict.values():
        if value != 1:
            count += 1
    return count