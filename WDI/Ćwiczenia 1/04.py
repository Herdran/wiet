d = int(input("Input a number: "))
s = 0
n = 0
k = 1

while s <= d:
    s += k
    n += 1
    k += 2

print(n-1)