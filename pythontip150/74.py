
def fun(words,index):
    soted_words = sorted(words, key=lambda word: word[index - 1])
    return soted_words