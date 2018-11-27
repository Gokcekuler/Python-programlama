data = [1,2,4,-1,3,4,-5,1]
i=0
aranan = int(input("Aranan değer: "))
while i<len(data):
    if data[i] == aranan:
        print("Aranan", aranan, "değeri", i, "pozisyonudna")
        break;

    i +=1
else:
    print("Bulamadık")







