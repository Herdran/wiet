x = 24
y = 56
z = 23
number = 1
while number < x*y*z:
    if number % x == 0 and number % y == 0 and number % z == 0:
        print("A wieloktortosc najmniejsa to", number)
        number = x*y*z
    number += 1
