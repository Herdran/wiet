x = int(input("Input a number you wish to get a square root of: "))
e = 0.000000000000001
a = 1
b = x
while a-b > e or b-a > e:
    a = (a+b)/2
    b = x//a
print(a)
