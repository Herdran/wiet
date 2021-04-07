def parent(i):
    return (i - 1) // 2


def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def build_heap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def heapify(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] < T[m]:
        m = l
    if r < n and T[r] < T[m]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)


def append_to_heap(T, value):
    i = len(T)
    T.append(value)
    while i > 0:
        if T[parent(i)] > value:
            # print("aaaaaa", T[parent(i)], T[i])
            T[parent(i)], T[i] = T[i], T[parent(i)]
            i = parent(i)
        else:
            i = 0



def heap_sort(T):
    build_heap(T)
    n = len(T)
    for i in range(n-1, -1, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)


T = [10, 3, 5, 11, 6, 1]
build_heap(T)
print(T)
append_to_heap(T, 0)
print(T)
heap_sort(T)
print(T)