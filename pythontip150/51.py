
def add_space_before_capital(word):
    # 初始化结果字符串
    result = ""
    # 遍历输入字符串的每个字符
    for i, char in enumerate(word):
        # 如果字符是大写字母，则在它前面添加空格
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char
    return result