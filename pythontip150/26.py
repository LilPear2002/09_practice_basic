
def fibonacci_number(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)