
def is_title(sentence):
    # 在此处编写代码
    my_list = sentence.split()
    for str in my_list:
        if str[0].islower():
            return False
    return True

# 从用户处获取输入
input_sentence = input()
# 调用函数
print(is_title(input_sentence))