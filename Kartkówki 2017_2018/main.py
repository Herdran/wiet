n = 9
x = 1
y = 1
i = 0

syf jprdl

list_fibonacci = [0] * 20
while x < 1000:
    list_fibonacci[i] = x
    y += x
    x = y - x
    i += 1
print(list_fibonacci)
number = n
a = True
b = False
while a == True:
    number += 1
    for i in range(len(list_fibonacci)):
        sum_ = 0
        for j in range(i, len(list_fibonacci)):
            if i == 2:
                print(sum_)
            sum_ += list_fibonacci[j]
            if sum_ == number:

                b = True
        if b == True:
            print("łaaa")
            a = False
        else:
            b = False
print(number)
