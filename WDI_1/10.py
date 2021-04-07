number = 1
x = 1
y = 0
while number < 1000000:
    while x < number:
        if number % x == 0:
            y += x
        x += 1
    if y == number:
        print(number)
    number +=1
    y = 0
    x = 1
