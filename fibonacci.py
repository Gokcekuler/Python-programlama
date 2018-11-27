a, b = 1, 1
print(a)
print(b)
i = 2
while i<=50:
    a,b = b, a+b
    print(b)
    i += 1
