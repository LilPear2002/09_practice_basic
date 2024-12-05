
def round_sum(a, b, c):
    return round(a) + round(b) + round(c)

def close_far(a, b, c):
    return (abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2) or (abs(a - b) >= 2 and abs(b - c) <= 1 and abs(a - c) >= 2) or (abs(a - b) >= 2 and abs(b - c) >= 2 and abs(a - c) <= 1)

def make_chocolate(small, big, goal):
    return -1 if goal > big * 5 + small else goal - big * 5 if goal % 5 <= small else goal - big * 5 - (5 - goal % 5)