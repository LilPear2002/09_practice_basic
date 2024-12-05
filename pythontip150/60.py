
def fun(sentence):
    words = sentence.split(" ")
    my_list = []
    for word in words:
        my_list.append(word[:-1] + word[-1].upper())
    return ' '.join(my_list)