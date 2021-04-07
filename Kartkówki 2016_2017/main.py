import random

n = 15
# MAX = [random.randint(100, 1000) for i in range(n)]
MAX = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
print(MAX)
length_final = 0
length = n - 1
for i in range(n):
    # print(i)
    x = i
    # while length > 1:
    length_current = 0
    for j in range(length - i + 1):
        # if MAX[x] != MAX[length - j]:
            # print(MAX[x], MAX[length - j])
            # length -= 1
        if MAX[x] == MAX[length - j]:
            # print(MAX[x], MAX[length - j], "jeessss")
            x += 1
            length_current += 1
            # print(length_current)
        if length_current > 1 and MAX[x - 1] != MAX[length - j]:
            # print(length_current, "aaaa")
            if length_final < length_current:
                length_final = length_current
            length_current = 0
    # print("łaaaaaaaaaaaa")
    length_current = 0
        # print("łaaaaaaaaaaaa")

            # print(x)


    length = n - i - 1
    # print(length)
print(length_final)