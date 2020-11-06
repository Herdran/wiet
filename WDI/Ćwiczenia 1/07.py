number = int(input("A number: "))

x = 0
y = 1
while y <= 1000000:
    if x*y == number:
        print("Jess, der ar numbas",x , y)
        break
    y = y + x
    x = y - x