
# 反向输出四位数
def reverse_output1(num):
    return num % 10 * 1000 + (num // 10) % 10 * 100 + (num // 100) % 10 * 10 + num // 1000

def reverse_output2(num):
    num = str(num)
    num = num[::-1]
    return int(num)

print(reverse_output1(1234))
print(reverse_output2(1234))
