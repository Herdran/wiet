a1 = int(input('n='))

digits = 0
a = 0
while a1 > 0:
    a = a * 10 + a1 % 10
    digits += 1
    a1 //= 10


i = 1
counter = 0
for i in range(1, 2 ** digits):
    b = i

    a2 = a
    to_check = 0

    for i2 in range(digits):
        if b % 2 == 1:
            to_check = to_check*10 + a2 % 10
        b //= 10
        a2 //= 10

    if to_check % 7 == 0:
        counter += 1
        #print to_check
print(counter)