from zmq.backend import first


def fun(first_list,second_list):
    for num in second_list:
        first_list.append(num)
    if first_list[1] > first_list[0]:
        first_list.sort()
        return first_list
    first_list.sort()
    first_list.reverse()
    return first_list