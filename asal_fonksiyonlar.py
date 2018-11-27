def asal_mi(x):
    i = 2
    while i*i < x:
        if x % i == 0:
            return False
        i += 1
    else:
        return True




