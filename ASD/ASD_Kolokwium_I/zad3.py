# Jakub Radek
# Program ten sprawdza minimalne prawdopodobieństwo a następnie dopasowuje ilość bucket-ów do tej wartości, następnie
# appendujete wartości do odpowiedniej tablicy zawierającej te buckety, sortuje algorytmem insertionsort a następnie
# nadpisuje podaną tablicę T tymi wartościami
# Szacowana złożoność tego algorytmu to n^2


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
    bucket_amount = P[0][2]
    for i in range(1, n):
        if P[i][0] < min_el:
            min_el = P[i][0]
        if P[i][2] < bucket_amount:
            bucket_amount = P[i][2]

    if (1/bucket_amount) % 2 == 0:
        bucket_amount = int(1//bucket_amount)
    else:
        bucket_amount = int(1//bucket_amount + 1)

    array = [[] for _ in range(bucket_amount)]
    for i in range(len(T)):
        array[min(int(T[i]-min_el), bucket_amount-1)].append(T[i])
    for i in range(bucket_amount):
        insertionsort(array[i])

    index = 0
    for i in array:
        for j in range(len(i)):
            T[index] = i[j]
            index += 1

    return T


runtests(SortTab)
