


def fun(str):
    char_list = list(str)
    countNumber = 0
    letterNumber = 0
    spaceNumber = 0
    otherNumber = 0
    for i in char_list:
        # if(float(i)>=0 and float(i)<=9):
        if(i.isdigit()):
            countNumber += 1
        elif(i.isalpha()):
            letterNumber += 1
        # elif(i==' '):
        elif(i.isspace()):
            spaceNumber += 1
        else:
            otherNumber += 1
    print(f"数字的个数为{countNumber},字母的个数为{letterNumber},空格的个数为{spaceNumber},其他字符的个数为{otherNumber}")


str = input('输入一串字符: \n')
fun(str)