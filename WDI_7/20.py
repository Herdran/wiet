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


def cw_20(list_):
    curr_checked = list_
    while curr_checked.next:
        curr = curr_checked
        while curr.next:
            prev = curr
            curr = curr.next
            if curr_checked.val[0] >= curr.val[0] and curr_checked.val[1] <= curr.val[1]:
                curr_checked.val[0] = curr.val[0]
                curr_checked.val[1] = curr.val[1]
                prev.next = curr.next
            elif curr_checked.val[0] <= curr.val[0] and curr_checked.val[1] >= curr.val[1]:
                curr_checked.val[0] = curr.val[0]
                curr_checked.val[1] = curr.val[1]
                prev.next = curr.next
            elif curr_checked.val[0] <= curr.val[0] and curr_checked.val[1] <= curr.val[1] and curr_checked.val[1] >= curr.val[0]:
                curr_checked.val[1] = curr.val[1]
                prev.next = curr.next
            elif curr_checked.val[1] >= curr.val[1] and curr_checked.val[0] >= curr.val[0] and curr.val[1] >= curr_checked.val[0]:
                curr_checked.val[0] = curr.val[0]
                prev.next = curr.next
            print_(list_)
        curr_checked = curr_checked.next
    return list_


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
list1_ = write(list1_, [15, 19])
list1_ = write(list1_, [2, 5])
list1_ = write(list1_, [7, 11])
list1_ = write(list1_, [8, 12])
list1_ = write(list1_, [5, 6])
list1_ = write(list1_, [13, 17])

print_(list1_)
print_(cw_20(list1_))

