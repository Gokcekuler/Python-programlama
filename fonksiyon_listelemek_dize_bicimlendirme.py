import math
x = 0.0
dx = 0.1
print("{:6s} {:6s}".format("x", "sin x"))
while x <= 1.0:
    print("{:1.4f} {:1.4f}".format(x, math.sin(x)))
    x += dx
