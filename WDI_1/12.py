x = 1023
y = 576
z = 209
number = x
while number > 0:
    if x % number == 0 and y % number == 0 and z % number == 0:
        print("A dzielnik najwienkszy", number)
        number = 0
    number -= 1
