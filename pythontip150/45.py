
def sum_numbers(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum
def sum_nums(nums):
    nums.sort()
    total = sum_numbers(nums[0], nums[-1])
    for num in nums:
        total -= num
    return total


