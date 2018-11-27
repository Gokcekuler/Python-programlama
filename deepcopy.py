import copy
a=[5,[4,9,3],7.1]
b=copy.deepcopy(a)
b[1][0]="merhaba"
print("a=",a)
print("b",b)






