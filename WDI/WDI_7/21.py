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


def cw_21(list_):
    prev = None
    curr = list_
    length = 1
    max_length = 1
    flag = True
    index = 0
    f_index = 0
    while curr.next:
        prev = curr
        curr = curr.next
        if prev.val < curr.val:
            length += 1
            if f_index == 0:
                f_index = index
        else:
            if length > max_length:
                max_length = length
                flag = True
            elif length == max_length:
                flag = False
            length = 1
            f_index = 0
        index += 1
    if length > max_length:
        max_length = length
        flag = True
    elif length == max_length:
        flag = False
    if flag:
        prev = None
        curr = list_
        if f_index == 0:
            for i in range(max_length):
                curr = curr.next
            return curr
        else:
            prev = list_
            curr = list_
            for i in range(f_index-1):
                prev = prev.next
                curr = curr.next
            for i in range(max_length):
                curr = curr.next
            prev.next = curr.next
            return list_
    else:
        return False


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
list1_ = write(list1_, 3)
list1_ = write(list1_, 4)
list1_ = write(list1_, 2)
list1_ = write(list1_, 3)

print_(list1_)
temp = (cw_21(list1_))
if temp:
    print_(temp)
