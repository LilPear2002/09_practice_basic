from collections import Counter


def min_removals_to_anagram(str1, str2):
    # 使用Counter计算第一个字符串中每个字符的出现次数
    count1 = Counter(str1)
    # 使用Counter计算第二个字符串中每个字符的出现次数
    count2 = Counter(str2)
    # 初始化移除字符计数器
    remove_count = 0
    # 遍历两个字符串中所有不同的字符
    for char in set(str1 + str2):
        # 累加每个字符在两个字符串中出现次数的差的绝对值
        remove_count += abs(count1[char] - count2[char])
    # 返回需要移除的字符总数
    return remove_count