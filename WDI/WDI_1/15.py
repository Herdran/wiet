from cmath import sqrt

x = sqrt(0.5)
y = x
delta = 1
while delta != 0:
    y = sqrt(0.5+0.5*y)
    z = x*y
    delta = z - x
    x = z
print("Pi ikłuls", 2 / x)
