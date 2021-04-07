class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def append(list_, n):
    prev = None
    curr = list_
    while curr is not None:
        prev = curr
        curr = curr.next

    if prev is None:
        list_ = Node(n)
        return list_

    curr = Node(n)
    prev.next = curr
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


list1_ = None
list1_ = append(list1_, 1)
list1_ = append(list1_, 2)
print_(list1_)
# print(contains_(list1_, 1))
# print(contains_(list1_, 3))
# removing(list1_, 1)
print_(list1_)
list1_ = append(list1_, 1)
list1_ = append(list1_, 2)
print_(list1_)