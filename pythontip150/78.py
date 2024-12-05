
def fun(s):
    # 遍历字符串的所有可能的子字符串长度
    for i in range(1, len(s) // 2 + 1):
        # 检查子字符串是否能够重复形成原始字符串
        if len(s) % i == 0:
            # 获取子字符串
            sub = s[:i]
            # 检查子字符串重复是否能够形成原始字符串
            if sub * (len(s) // i) == s:
                # 返回重复次数
                return len(s) // i
    # 如果没有找到这样的子字符串，返回1
    return 1