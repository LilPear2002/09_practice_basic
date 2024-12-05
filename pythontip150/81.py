def check_consecutive_sum(n):
    # 此处写代码
    # 如果n是2的幂，则返回False
    if n & (n - 1) == 0:
        return False
    # 从最小的正整数1开始尝试
    start = 1
    end = 1
    current_sum = 1

    # 使用滑动窗口方法来找到连续的正整数序列
    while start <= n // 2:
        if current_sum < n:
            # 如果当前和小于n，增加end并更新当前和
            end += 1
            current_sum += end
        elif current_sum > n:
            # 如果当前和大于n，减少start并更新当前和
            current_sum -= start
            start += 1
        else:
            # 如果当前和等于n，返回True
            return True
    # 如果没有找到合适的序列，返回False
    return False