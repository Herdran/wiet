from random import randint, seed


def mergesort(T):
    length = len(T)
    if length <= 1:
        return T
    elif length == 2:
        if T[0] > T[1]:
            T[0], T[1] = T[1], T[0]
        return T
    tableft = mergesort(T[:length//2])
    tabright = mergesort(T[length//2:])
    i = 0
    j = 0
    len_i = length // 2
    len_j = length - len_i

    while i < len_i and j < len_j:
        if tableft[i] < tabright[j]:
            T[i+j] = tableft[i]
            i += 1
        else:
            T[i+j] = tabright[j]
            j += 1
    while j < len_j:
        T[i+j] = tabright[j]
        j += 1
    while i < len_i:
        T[i + j] = tableft[i]
        i += 1
    return T


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")