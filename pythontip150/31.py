from math import lcm

def smallest_multiple(n):
    """找出能被1到n所有数字整除的最小正数"""
    # 初始化结果变量为1，用于后续计算最小公倍数
    result = 1
    # 遍历从2到n的所有整数，计算这些整数的最小公倍数
    for i in range(2, n + 1):
        # 使用result存储当前计算得到的最小公倍数
        result = lcm(result, i)
    # 返回从2到n所有整数的最小公倍数
    return result