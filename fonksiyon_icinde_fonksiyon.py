x=10
print("x =", x)
def f():
    x=20
    print("f içinde x=",x)
    def g():
        x=30
        print("g içinde x=", x)
    g()

f()












