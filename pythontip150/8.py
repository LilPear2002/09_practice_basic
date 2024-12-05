
def find_unique_number(num_list):
    if not num_list:
        return None
        # 如果列表只有一个数字，返回该数字
    if len(num_list) == 1:
        return num_list[0]
        # 使用字典来统计每个数字出现的次数
    count_dict = {}
    for num in num_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    # 找出出现次数为1的数字
    for num, count in count_dict.items():
        if count == 1:
            return num
    # 如果不存在这样的数字，返回None
    return None