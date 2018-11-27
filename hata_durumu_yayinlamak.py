def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError("Negatif deger")
    p=1
    for i in range(1,x+1):
        p *=i
    return p

for x in [5, -5, "abc", 5]:
    try:
        y=faktoriyel(x)
    except ValueError as e:
        print(x,": ",e)
        continue
    print(y)

