
# 求斐波那契数列的第n项
#递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 非递归
def fib2(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

print(fib(6))
print(fib2(7))