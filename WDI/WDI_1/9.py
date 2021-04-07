number = int(input("A number: "))
x = 1
print("Dzielniki to:", end="")
while x <= number:
    if number % x == 0:
        print("",x, end="")
    x += 1