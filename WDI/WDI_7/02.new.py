class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def append(list_, n):
    prev = None
    curr = list_
    while curr.next is not None:
        prev = curr
        curr = curr.next

    if prev is None:
        list_.next = Node(n)
        return list_

    curr.next = Node(n)
    prev.next = curr
    return list_


def print_(list_):
    curr = list_
    while curr.next is not None:
        print(curr.next.val, end=' -> ')
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



def append_to_index(list_, n, index):
    i = -1
    prev = None
    curr = list_
    while i < index:
        i += 1
        prev = curr
        curr = curr.next
    curr.val = n
    prev.next = curr


def print_index(list_, index):
    i = -1
    curr = list_
    while i < index:
        i += 1
        curr = curr.next
    print(curr.val)

list1_ = Node()
append(list1_, 1)
append(list1_, 2)
print_(list1_)
# print(contains_(list1_, 1))
# print(contains_(list1_, 3))
removing(list1_, 1)
print_(list1_)
list1_ = append(list1_, 1)
list1_ = append(list1_, 2)
print_(list1_)
append_to_index(list1_, 5, 1)
print_(list1_)
print_index(list1_, 2)