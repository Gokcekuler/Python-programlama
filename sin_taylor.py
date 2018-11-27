import math
x = 0.0
dx = 0.1
print("{:6s} {:6s} {:6s} {:6s} {:6s}".format("x", "f1", "f2", "f3", "sin x"))
while x <= 1.0:
    f1 = x - x**3 /6
    f2 = f1 + x**5/120
    f3 = f2 + x**7/5040
    print("{:1.4f} {:1.4f} {:1.4f} {:1.4f} {:1.4f}".format(x, f1, f2, f3, math.sin(x)))
    x += dx
