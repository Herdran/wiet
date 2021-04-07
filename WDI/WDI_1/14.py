from math import pi

x = 3 * pi
x1 = 0
x2 = 1
n = 0
f = 1
sum_ = 0
while n < 20:
    for i in range(1, 2 * n + 1):
        f = f * i
    x1 = x2
    x2 = ((-1) ** n) * (x ** (2 * n)) / f
    sum_ += x2
    n += 1
    f = 1
print(sum_)
