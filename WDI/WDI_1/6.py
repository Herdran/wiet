a = 4
b = 5
x = 0
e = 0.000000000001
while x**x - 2020 > e or 2020 - x**x > e:
    x = (a + b) / 2
    if (a ** a - 2020) * (x ** x - 2020) < 0:
        b = x
    if (b ** b - 2020) * (x ** x - 2020) < 0:
        a = x
print(x)
