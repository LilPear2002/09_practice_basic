
def fun(string):
    sum = 0
    str = string.split(" ")
    for word in str:
        for str in word:
            if str.isalpha():
                sum += ord(str)
    if sum % 2 == 0:
        return True
    return False