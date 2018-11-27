while True:
    x=input("Bir sayi girin: ")
    if not x:
        break
    try:
        y=1/float(x)
    except ValueError:
        print("Gecersiz sayi")
        continue
    except ZeroDivisionError:
        print("Sifira bolme")
        continue
    print(y)


