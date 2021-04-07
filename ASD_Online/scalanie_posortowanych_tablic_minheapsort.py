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
    deleted = None
    m = i
    if l < n and T[l] < T[m]:
        m = l
    if r < n and T[r] < T[m]:
        m = r
    if m != i:
        deleted = m
        # print(deleted, l, r, i, m, n)
        # print(T)
        T[i], T[m] = T[m], T[i]
        # print(T)
        heapify(T, n, m)
    print(T)
    return deleted


def append_to_heap(T, value):
    i = len(T)
    T.append(value)
    while i > 0:
        if T[parent(i)] > value:
            T[parent(i)], T[i] = T[i], T[parent(i)]
            i = parent(i)
        else:
            i = 0



def heap_sort(T):
    build_heap(T)
    n = len(T)
    deleted = None
    for i in range(n-1, -1, -1):
        T[i], T[0] = T[0], T[i]
        tmp = heapify(T, i, 0)
        # print(T)
        if tmp:
            deleted = tmp
    return deleted


def merge_arrays(A, n):
    T = []
    heap = [0]*n
    depth = [0]*n
    for i in range(n):
        heap[i] = A[i][0]
    deleted = heap_sort(heap)
    print(deleted, heap, "jdsjds")
    while heap:
        T.append(heap[0])
        heap.pop(0)
        print(heap, "aa")
        # print(T)
        depth[deleted] += 1
        append_to_heap(heap, A[deleted][depth[deleted]])
        print(heap, "bbbbbb")
        print(T)

# T = [10, 3, 5, 11, 6, 1]
# build_heap(T)
# print(T)
# append_to_heap(T, 0)
# print(T)
# heap_sort(T)
# print(T)

A = [[1, 2, 10, 20], [5, 32, 50], [0, 25, 26, 26, 51]]

T = merge_arrays(A, len(A))
