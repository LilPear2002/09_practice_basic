
def swap_dict(d):
    # 此处编写代码
    # 创建一个新的空字典来存储交换后的键值对
    swapped = {}
    for key, value in d.items():
        # 如果值已经作为键存在于新字典中，将原键添加到对应的列表中
        if value in swapped:
             swapped[value].append(key)
        # 如果值不在新字典中，直接添加
        else:
            swapped[value] = [key]
    return swapped