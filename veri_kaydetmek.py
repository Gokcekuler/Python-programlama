import pickle
x=3.14159
L=[1,3,2,5,4]
D={"abc": 123, "def":456}
def fon(x):
    return x*x
with open("data.p", "wb") as f:
    pickle.dump(x,f)
    pickle.dump(L,f)
    pickle.dump(D,f)
    pickle.dump(fon,f)

with open("data.p", "rb") as f:
    y=pickle.load(f)
    print(y)
    J=pickle.load(f)
    print(J)
    F=pickle.load(f)
    print(F)
    G=pickle.load(f)
    print(G(y))


