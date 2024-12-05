
def fun(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return fun(string[1:-1])