
def shift_char(word):
    # 将单词中的每个字符转换为它的下一个字符
    return ''.join(chr(ord(c) + 1) for c in word)