
# 给定一个数组nums(里面均为数字)，如果数组中存在一个连续序列1,2,3 则返回True 否则 False
def fun(nums : list[int]):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False