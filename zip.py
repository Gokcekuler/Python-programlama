import zipfile
with zipfile.ZipFile("arsiv.zip","w") as z:
    z.write("denemek.txt")
    z.write("yalanci_veri.json")


with zipfile.ZipFile('arsiv.zip') as z:
    with z.open('denemek.txt') as f:
        print(f.read().decode("utf-8"))

