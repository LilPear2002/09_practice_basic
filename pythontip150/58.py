
def fun(n):
    binary_string = bin(n)[2:]
    my_list = list(binary_string)
    my_list.reverse()
    binary_string = ''.join(my_list)
    num = int(binary_string,2)
    return num