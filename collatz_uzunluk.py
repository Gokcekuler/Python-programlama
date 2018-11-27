def collatz(n):   
    enbüyük =n
    uzunluk = 0
    while n<1000000:
        while n > 1:
            if n % 2==0:
                n = n/2
            else:
                n = 3*n + 1

            uzunluk += 1
    return uzunluk



