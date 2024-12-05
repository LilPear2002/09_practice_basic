def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


#输入数据
nums = eval(input())
#调用函数打印结果
print(array_count9(nums))