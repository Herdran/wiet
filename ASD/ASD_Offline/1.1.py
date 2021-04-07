from random import randint, seed


def mergesort(T):
    length = len(T)
    if length <= 1:
        return T, 0
    elif length == 2:
        if T[0] > T[1]:
            T[0], T[1] = T[1], T[0]
            return T, 1
        return T, 0
    inv_count = 0
    tableft, x = mergesort(T[:length//2])
    tabright, y = mergesort(T[length//2:])
    inv_count += x + y
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
            inv_count += len_j - j
            j += 1
    while j < len_j:
        T[i+j] = tabright[j]
        j += 1
        inv_count += 1
    while i < len_i:
        T[i + j] = tableft[i]
        i += 1
    return T, inv_count


seed(44)

n = 10
T = [randint(1, 10) for i in range(10)]
print("przed sortowaniem: T =", T)
T, inv_counter = mergesort(T)
print("po sortowaniu    : T =", T, inv_counter)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")