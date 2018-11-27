toplam=0
while True:
    x= int(input("Bir sayi girin"))
    if x == -99:
        break
    if x < 0 or x > 100:
        print("0-100 arası olmalı")
        continue
    toplam += x
print("Toplam:", toplam)

