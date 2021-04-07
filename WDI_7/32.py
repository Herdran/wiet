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


def cw_32(list1, list2):
    f1 = list1
    f2 = list2
    first = None
    while f1 or f2:
        if f1 and f2:
            first = write(first, f1.val - f2.val)
            f1 = f1.next
            f2 = f2.next
        elif f1:
            first = write(first, f1.val)
            f1 = f1.next
        elif f2:
            first = write(first, f2.val)
            f2 = f2.next
    prev = None
    curr = first
    print_(first)
    while curr:
        if curr.val == 0:
            temp = curr.next
            flag = False
            while temp:
                if temp.val != 0:
                    flag = True
                temp = temp.next
            if not flag:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        else:
            prev = curr
            curr = curr.next


    return first


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
list1_ = write(list1_, 7)
list1_ = write(list1_, 3)
list1_ = write(list1_, 2)
list2_ = None
list2_ = write(list2_, 9)
list2_ = write(list2_, 3)
list2_ = write(list2_, 2)

list3_ = (cw_32(list1_, list2_))
print_(list1_)
print_(list2_)
print_(list3_)
