
def count_sublists(list_input):
    """
    统计输入列表中列表元素的数量。
    """
    # 初始化计数器
    count = 0
    # 遍历列表中的每个元素
    for element in list_input:
        # 检查元素是否是列表（即子列表）
        if isinstance(element, list):
            count += 1
    return count
