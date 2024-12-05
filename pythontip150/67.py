
def binary_to_int(bin_tuple):
    # 将二进制元组转换为整数
    # bin_tuple: 一个包含多个整数的元组，每个整数代表二进制数的一位
    # 返回值: 转换后的整数
    return int(''.join(map(str, bin_tuple)), 2)