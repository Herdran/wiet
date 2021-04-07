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
    while curr.next is not None:
        if curr.val == n:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next


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


def cw_5(list_):
    curr = list_
    temp = [None]*10
    while curr:
        temp[curr.val % 10] = write(temp[curr.val % 10], curr.val)
        curr = curr.next
    first = None
    for i in range(10):
        while temp[i]:
            first = write(first, temp[i].val)
            temp[i] = temp[i].next
    print_(first)


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


list1_ = None
list1_ = write(list1_, 10)
list1_ = write(list1_, 11)
list1_ = write(list1_, 12)
list1_ = write(list1_, 13)
list1_ = write(list1_, 14)
list1_ = write(list1_, 15)
list1_ = write(list1_, 16)
list1_ = write(list1_, 17)
list1_ = write(list1_, 18)
list1_ = write(list1_, 19)
list1_ = write(list1_, 20)
print_(list1_)
cw_5(list1_)
