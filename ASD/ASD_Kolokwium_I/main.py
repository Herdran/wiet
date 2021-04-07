from zad3testy import runtests


def insertionsort(T):
    j = 0
    for i in range(1, len(T)):
        e = T[i]
        j = i - 1
        while j >= 0 and T[j] > e:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = e


def SortTab(T, P):
    n = len(P)
    min_el = P[0][0]
    # max_el = P[0][1]
    bucket_amount = P[0][2]
    print(P)
    for i in range(1, n):
        if P[i][0] < min_el:
            min_el = P[i][0]
        # if P[i][1] > max_el:
        #     max_el = P[i][1]
        if P[i][2] < bucket_amount:
            bucket_amount = P[i][2]

    if (1/bucket_amount)%2 == 0:
        bucket_amount = int(1//bucket_amount)
    else:
        bucket_amount = int(1//bucket_amount + 1)

    # print(bucket_amount, min_el, max_el)


    array = [[] for _ in range(bucket_amount)]
    for i in range(len(T)):
        array[min(int(T[i]-min_el), bucket_amount-1)].append(T[i])

    print(array)
    for i in range(bucket_amount):
        insertionsort(array[i])

    index = 0
    for i in array:
        for j in range(len(i)):
            T[index] = i[j]
            index += 1

    return T

















# P = [(1, 5, 0.75), (4, 8, 0.25)]
# T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
# SortTab(T, P)
runtests(SortTab)
