
def find_numbers(n, m):
    result = []

    for i in range(n + 1, m):
        if (i - 1) * i * (i + 1) % 5 == 0:
            result.append(i)
            if len(result) == 3:
                break

    # 返回结果，并确保结果列表的长度为3
    # 如果结果列表的长度小于3，则通过添加-1来进行填充
    return result + [-1] * (3 - len(result))

# 测试样例
print(find_numbers(10, 200))  # 输出: [14, 15, 16]
print(find_numbers(1, 6))     # 输出: [4, 5, -1]
