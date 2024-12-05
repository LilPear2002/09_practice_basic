
def fun(num_list):
    num_list.sort()
    for i in range(1, len(num_list) - 1):
        if num_list[i] != num_list[i - 1] + 1:
            return False
    return True