degisken= "x" 
formul= input("Bir matematiksel formul girin:")
kod= """
for {0} in range(10):
    print( {0}, {1}) """.format(degisken, formul)
print(kod)
exec(kod)

print(globals())



