
def fun(word1,word2):
    count_dict = {}
    for char in word1:
        if char in word2:
            count_dict[char] = 1
    count = 0
    for key in count_dict.keys():
        count += 1
    return count