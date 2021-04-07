import random
"""JEST ŹLE OFC"""
n = 15
# MAX = [random.randint(100, 1000) for i in range(n)]
MAX = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
print(MAX)
length_final = 0
length = n - 1
for i in range(n):
    x = i
    length_current = 0
    for j in range(length - i + 1):
        print(MAX[x], MAX[length - j])
        if length_current > 1 and MAX[x - 1] != MAX[length - j]:
            if length_final < length_current:
                length_final = length_current
            # x = i
            length_current = 0
        # if MAX[x] != MAX[length - j]:
        #     length_current = 0
            # print(MAX[x], MAX[length - j])
            # length -= 1
        if MAX[x] == MAX[length - j]:
            x += 1
            length_current += 1
    length_current = 0
    length = n - i - 1
print(length_final)