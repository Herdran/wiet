number = int(input("A number: "))
x = 2
while x < number:
    if number % x == 0:
        print("Not a prajm")
        x = number
    x += 1
if x == number:
    print("A prajm")