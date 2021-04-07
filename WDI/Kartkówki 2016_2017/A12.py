import random
n = 20
MAX = [random.randint(1, 1000) for i in range(n)]
print(MAX)

list_of_biggest_ten = [0] * 10
for i in range(10):
    biggest = 0
    for j in range(n):
        if MAX[j] > biggest and (i == 0 or list_of_biggest_ten[i - 1] > MAX[j]):
            biggest = MAX[j]
    list_of_biggest_ten[i] = biggest
print(list_of_biggest_ten)
