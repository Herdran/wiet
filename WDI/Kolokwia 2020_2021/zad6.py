# Jakub Radek
# Funkcja iloczyn działa tak, że sprawdza po kolei każdy element z pierwszej podanej tablicy, i równocześnie wykorzystuje
# funkcję contains żeby sprawdzić czy element ten zawiera się również w pozostałych listach. Jeśli tak, to ta wartość
# jest wpisywana funkcją write do nowej listy, pętla wykonuje się do momentu jak sprawdzi wszystkie elementy z pierwszej
# listy. Zostawiłem w komentarzach funkcję print_ a także mój testowy przypadek, który zwraca jednoelementową listę
# zawierającą w sobie cyfrę "2", na wypadek gdyby moja interpretacja tej metody nie była dokładnie taka jak powinna.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# def print_(list_):
#     curr = list_
#     while curr is not None:
#         print(curr.val, end=' --> ')
#         curr = curr.next
#     print()


def write(first, el):
    if not first:
        return Node(el)
    prev = None
    curr = first
    while curr:
        prev = curr
        curr = curr.next
    prev.next = Node(el)
    return first


def contains_(list_, n):
    curr = list_
    while curr:
        if curr.val == n:
            return True
        curr = curr.next
    return False


def iloczyn(z1, z2, z3):
    first = None
    el_1 = z1
    el_2 = z2
    el_3 = z3

    while el_1 is not None:
        if contains_(el_2, el_1.val) and contains_(el_3, el_1.val):
            first = write(first, el_1.val)
        el_1 = el_1.next
    return first


# z1 = None
# z1 = write(list1_, 2)
# z1 = write(list1_, 4)
# z1 = write(list1_, 5)
# z2 = None
# z2 = write(list2_, 1)
# z2 = write(list2_, 2)
# z2 = write(list2_, 10)
# z3 = None
# z3 = write(list2_, 2)
# z3 = write(list2_, 6)
# z3 = write(list2_, 7)

# n = iloczyn(z1, z2, z3)
# print_(n)