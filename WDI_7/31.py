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
    while curr:
        if curr.val == n:
            if prev:
                prev.next = curr.next
                break
            else:
                list_.val = list_.next.val
                list_.next = list_.next.next
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


def cw_31(list1, list2, list3):
    curr = list1
    while curr:
        if curr.val > 0 and curr.val % 2 == 0:
            list2 = write(list2, curr.val)
        elif curr.val < 0 and curr.val % 2 == 1:
            list3 = write(list3, curr.val)
        curr = curr.next
    return list2, list3

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
list1_ = write(list1_, 2)
list1_ = write(list1_, -3)
list1_ = write(list1_, 5)
list1_ = write(list1_, 8)
list1_ = write(list1_, -11)
list2_ = None
list3_ = None


list2_, list3_ = (cw_31(list1_, list2_, list3_))
print_(list1_)
print_(list2_)
print_(list3_)
