
def love6(a, b):
  """
  The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
  """
  return a==6 or b==6 or abs(a-b)==6 or a+b==6

def lone_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
    """
    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c