from random import randint
L=list(range(1,1000001))
s=set(L)
%%timeit
n=randint(1,2000000)
n in L

