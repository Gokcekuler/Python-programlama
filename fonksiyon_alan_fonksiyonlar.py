def fntoplam(f,a,b):
    i=a
    toplam =0
    while i<=b:
        toplam += f(i)
        i+=i
    return toplam
def f1(x):
    return 1.0/x
def f2(x):
    return 2.0**-x




fntoplam(f1,1,10) 
