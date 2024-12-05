
# 递归函数，用于找到列表中最大的数
def find_highest_number(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        return max(numbers_list[0], find_highest_number(numbers_list[1:]))
