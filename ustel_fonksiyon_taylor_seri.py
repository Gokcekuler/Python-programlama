def üstel(x, hata = 1e-8, maxterim = 20):
    n = 1
    sonterim = 1 
    toplam = sonterim
    while sonterim >= hata:
        if n > maxterim:
            print("{} terimde yakınsama sağlanamadı".format(maxterim))
            break
        sonterim = sonterim * x/n 
        toplam += sonterim
        n += 1
    return toplam


