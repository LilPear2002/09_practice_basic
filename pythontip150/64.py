
def fun(word1,word2):
    list1 = []
    for char in word1:
        if char in word2 and char not in list1:
            list1.append(char)
    list1.sort()
    str1 = ''.join(list1)
    return str1.lower()
