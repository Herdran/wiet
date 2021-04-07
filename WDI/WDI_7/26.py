class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_(list_):
    curr = list_
    while curr is not None:
        print(curr.val, end=' -> ')
        curr = curr.next
    print()


def removing(list_, n):
    prev = None
    curr = list_
    while curr is not None:
        if curr.val == n:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next


def contains_(list_, n):
    curr = list_
    while curr:
        if curr.val == n:
            return True
        curr = curr.next
    return False


def scal(f1, f2):
    first = None
    el_1 = f1
    el_2 = f2

    while el_1 is not None:
        first = write(first, el_1.val)
        el_1 = el_1.next
    while el_2 is not None:
        first = write(first, el_2.val)
        el_2 = el_2.next
    return first


def reverse_(first):
    if first is None:
        return first

    p = None
    r = first
    while r is not None:
        next = r.next
        r.next = p
        p = r
        r = next
    return p


def cw_26(f1, f2):
    base = f1
    curr = f2
    while curr:
        if not contains_(base, curr.val):
            return False
        curr = curr.next
    return True


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


# def write_cycle(first, el):
#     curr = first
#     while curr.next:
#         prev = curr
#         curr = curr.next
#     curr.next = prev
#     return first

list1_ = None
list1_ = write(list1_, 2)
list1_ = write(list1_, 4)
list1_ = write(list1_, 5)
list2_ = None
list2_ = write(list2_, 4)
list2_ = write(list2_, 2)
# list1_ = write_cycle(list1_, 3)
# list1_.next.next.next = list1_.next

# print_(list1_)
print(cw_26(list1_, list2_))
# if temp:
#     print_(temp)
