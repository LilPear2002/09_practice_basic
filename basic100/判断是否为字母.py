
def judge1(str):
    if(a >= 'a' and a <= 'z' or a >= 'A' and a <= 'Z'):
        return True
    else:
        return False
        
def judge2(str):
    return a.isalpha()
            
a = input("请输入一个字符：")
print(judge1(a))
print(judge2(a))