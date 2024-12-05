
# 返回 int 列表nums请返回平均值，
# 但忽略数组中的最大值和最小值。如果最小值有多个副本，则只忽略一个副本，对于最大值也是如此

def centered_average(nums):
    nums.sort()
    nums.pop(0)
    nums.pop()
    return sum(nums) / len(nums)