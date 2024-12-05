
def check_double_base_palindrome(number):
    # 此处编写代码
    binary = int(bin(number)[2:])
    return judge(number) and judge(binary)

def judge(number):
    return str(number) == str(number)[::-1]


# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))