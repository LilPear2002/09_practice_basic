def count_binary_ones(num):
    # 将给定的整数转换为二进制字符串，去掉前缀'0b'
    binary_str = bin(num)[2:]
    # 初始化计数器，用于统计二进制字符串中'1'的数量
    count = 0
    # 遍历二进制字符串中的每一位
    for digit in binary_str:
        # 如果当前位是'1'，则计数器加一
        if digit == '1':
            count += 1
    # 返回统计结果，即二进制字符串中'1'的数量
    return count