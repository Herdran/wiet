number = 1
number2 = 1
x = 1
y = 0
z = 0
while number < 1000000:
    while x < number:
        if number % x == 0:
            y += x
        if number2 % x == 0:
            z += x
        x += 1
    if y == number2 and z == number and number != number2:
        print(number, number2)
    if number2 < 1000000:
        number2 += 1
    else:
        number += 1
        number2 = number
    z = 0
    y = 0
    x = 1
