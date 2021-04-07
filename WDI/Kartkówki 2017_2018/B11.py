def if_sum_fibonacci(number, list_fibonacci):
    for i in range(len(list_fibonacci)):
        sum_ = 0
        for j in range(i, len(list_fibonacci)):
            sum_ += list_fibonacci[j]
            if sum_ == number:
                return True
    return False


n = 14
x = 1
y = 1
i = 0
list_fibonacci = [0] * 20
while x < 1000:
    list_fibonacci[i] = x
    y += x
    x = y - x
    i += 1
number = n
z = True
while z == True:
    number += 1
    z = if_sum_fibonacci(number, list_fibonacci)
print(number)
