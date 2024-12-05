
def fun(num_list,n):
    if n > len(num_list):
        return None
    num_list.sort()
    return num_list[n - 1]