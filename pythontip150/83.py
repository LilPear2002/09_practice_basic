
def fun(sub_string, main_string):
    sub_set = set(sub_string)
    main_set = set(main_string)

    # 检查sub_set是否是main_set的子集
    return sub_set.issubset(main_set)