def summa(a, b):
    if a == 0:
        return b
    else:
        return summa(a-1, b+1)
