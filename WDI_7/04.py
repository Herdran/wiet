class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def append_(list_, n):
    prev = None
    curr = list_
    while curr is not None and curr.val < n:
        prev = curr
        curr = curr.next

    new_el = Node(n)

    if prev is None:
        new_el.next = curr
        return new_el

    new_el.next = curr
    prev.next = new_el
    return list_


def print_(list_):
    curr = list_
    while curr is not None:
        print(curr.val, end=' -> ')
        curr = curr.next
    print()


def contains_(list_, n):
    curr = list_
    while curr.next is not None:
        if curr.val == n:
            return True
        curr = curr.next
    return False


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
        first = append_(first, el_1.val)
        el_1 = el_1.next
    while el_2 is not None:
        first = append_(first, el_2.val)
        el_2 = el_2.next
    return first


def reverse_chwast(first):
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


def odwracanie(list_):
    first = None
    el_1 = list_

    while el_1 is not None:
        first = append_reverse(first, el_1.val)
        el_1 = el_1.next
    return first


def append_reverse(list_, n):
    prev = None
    curr = list_
    while curr is not None and curr.val > n:
        prev = curr
        curr = curr.next

    new_el = Node(n)

    if prev is None:
        new_el.next = curr
        return new_el

    new_el.next = curr
    prev.next = new_el
    return list_


list1_ = None
list1_ = append_(list1_, 2)
list1_ = append_(list1_, 1)
print_(list1_)
# print(contains_(list1_, 1))
# print(contains_(list1_, 3))
# removing(list1_, 1)
print_(list1_)
list1_ = append_(list1_, 1)
list1_ = append_(list1_, 2)
list1_ = append_(list1_, 0)
print_(list1_)

list2_ = None
list2_ = append_(list2_, 30)
list2_ = append_(list2_, 20)
list2_ = append_(list2_, 1)
print_(list2_)
print_(scal(list1_, list2_))
print_(odwracanie(scal(list1_, list2_)))