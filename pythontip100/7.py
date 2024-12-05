class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError("参数不能为空")
        if nums == []:
            raise ValueError("参数不能为空")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == val:
                    return [i, j]