T = int(input())
for i in range(T):
    number = int(input())
    if number > 45:
        print(-1)
    elif number < 10:
        print(number)
    else:
        x = 0
        starting_number = 9
        while number > 0:
            if number - starting_number >= 0:
                number -= starting_number
                x *= 10
                x += starting_number
            starting_number -= 1
        y = 0
        while x > 0:
            y *= 10
            y += x % 10
            x //= 10
        print(y)
