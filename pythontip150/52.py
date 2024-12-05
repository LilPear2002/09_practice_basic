
def fun(sentence):
    words = sentence.split(" ")
    length = 0
    longest_word = ""
    for word in words:
        if len(word) > length:
            length = len(word)
            longest_word = word
    return longest_word