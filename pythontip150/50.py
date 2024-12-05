
def fun(sentence,char):
    sentence = sentence.lower()
    my_list = sentence.split(" ")
    count_list = []
    for str in my_list:
        count = 0
        for i in str:
            if i == char:
                count += 1
        count_list.append(count)
    return count_list