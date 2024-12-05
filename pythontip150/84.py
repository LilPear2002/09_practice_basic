def flatten_list(list_of_lists):
    # 在此处编写你的代码
    # 创建一个空列表来存储扁平化后的元素
    flat_list = []

    # 定义一个递归函数来处理嵌套列表
    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                # 如果元素是列表，递归调用flatten函数
                flatten(item)
            else:
                # 如果元素不是列表，添加到flat_list中
                flat_list.append(item)

    # 调用递归函数
    flatten(list_of_lists)

    return flat_list