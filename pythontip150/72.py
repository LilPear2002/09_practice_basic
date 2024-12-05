
def sort_by_last_char(sentence):
    words = sentence.split()
    # 根据单词的最后一个字母对单词列表进行排序
    sorted_words = sorted(words, key=lambda word: word[-1])
    return ' '.join(sorted_words)