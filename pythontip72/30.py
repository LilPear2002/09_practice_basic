
def fun(a,b):
    short = a if len(a) < len(b) else b
    long = b if len(b) > len(a) else a
    return short + long + short
