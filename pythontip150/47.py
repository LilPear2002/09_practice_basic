
def get_missing_letters(word_string):
    """
    Write a function to get all the missing letters in a given string.
    >>> get_missing_letters("abce")
    "dfhijklmnoqrstuvwxyz"
    >>> get_missing_letters("abcdefghijklmnopqrstuvwxyz")
    ""
    """

    # 定义一个包含所有小写字母的字符串
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # 计算并返回一个字符串，该字符串是字母表中所有不在word_string中的字母
    # 首先，使用set(alphabet).difference(word_string)找到在字母表中但不在word_string中的字母
    # 然后，使用"".join(sorted(...))将这些字母排序并连接成一个字符串
    return "".join(sorted(set(alphabet).difference(word_string)))