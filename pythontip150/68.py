
def fun(num_list,target_num):
    num_list.sort()
    left, right = 0, len(num_list) - 1
    while left < right:
        sum = num_list[left] + num_list[right]
        if sum == target_num:
            return True
        elif sum < target_num:
            left += 1
        else:
            right -= 1
    return False