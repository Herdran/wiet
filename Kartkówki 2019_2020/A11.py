def a11(t1, t2):
    amount = 24
    length_a = amount - 1
    sum_1 = 0
    sum_2 = 0
    a = False
    b = False
    while length_a > 0:
        for i in range(length_a):
            while a != True and length_a + i < len(t1):
                for j in range(i, length_a + i):
                    sum_1 += t1[j]
                a = if_power_of(sum_1)
                i += 1
                sum_1 = 0
            if a != True:
                length_a -= 1
        shift = 0
        while b != True and shift + amount - length_a < len(t2):
            for j in range(shift, shift + amount - length_a):
                sum_2 += t2[j]
            b = if_power_of(sum_2)
            shift += 1
            sum_2 = 0

        if a == b == True:
            return True
        else:
            a = False
            b = False
            length_a -= 1
    return False


def if_power_of(x):
    y = 2
    z = 2
    while y < x:
        while y ** z <= x:
            if y ** z == x:
                return True
            z += 1
        y += 1
        z = 2
    return False

# t1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 24]
t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
t2 = [9, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# print(if_power_of(25))
print(a11(t1, t2))