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


def cw_9(list_):
    prev = None
    curr = list_
    while curr:
        prev = curr
        curr = curr.next
    prev.val += 1


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
list1_ = write(list1_, 1)
list1_ = write(list1_, 2)
list1_ = write(list1_, 3)

print_(list1_)
cw_9(list1_)
print_(list1_)
