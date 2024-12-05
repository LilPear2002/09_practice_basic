from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

c = Counter(nums)
count = 0

for key,value in c.items():
    if key > value:
        count += value
    else:
        count += value - key

print(count)