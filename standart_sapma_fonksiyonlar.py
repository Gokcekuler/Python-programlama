import math   
def stsapma(x1, x2, *y):
    N = len(y) + 2 
    toplam = x1 + x2
    for z in y:
        toplam += z
    ort = toplam/N

    karetoplam = (x1-ort)**2 + (x2-ort)**2
    for z in y:
        karetoplam += (z-ort)**2
    stsap = math.sqrt(karetoplam/(N-1))
    return stsap

