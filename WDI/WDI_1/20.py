e = 0.000000000000001
a = 1
b = 3

while abs(a-b) > e:
    a_temp = a
    a = (a*b) ** 0.5
    b = (a_temp+b)/2
print(a)
