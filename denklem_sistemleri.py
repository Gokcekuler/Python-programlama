import math

a,b,c = 1000, 0, 0
N = a+b+c

lam_a = math.log(2) / 6.57 # I-135, 1/saat biriminde
lam_b = math.log(2) / 9.14 # Xe-135, 1/saat biriminde
t = 0


print("{:>6s} {:>6s} {:>6s} {:>6s}".format("saat", "I","Xe","Cs"))


while t <= 20:
    print("{:6d} {:6d} {:6d} {:6d}".format(t, int(a), int(b), int(c)))
    a = (1-lam_a)*a
    b = (1-lam_b)*b + lam_a*a
    c = N-a-b
    t += 1
