
def fun(nested_tuples):
    count_dict = {}
    for i in range(len(nested_tuples)):
        for j in range(len(nested_tuples[i])):
            if nested_tuples[i][j] in count_dict:
                count_dict[nested_tuples[i][j]] += 1
            else:
                count_dict[nested_tuples[i][j]] = 1
    my_list = []
    for key in count_dict.keys():
        my_list.append(key)
    my_list.sort()
    return my_list