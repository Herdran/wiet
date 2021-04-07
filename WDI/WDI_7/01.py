class Node:
    def __init__(self):
        self.val = None
        self.next = None


class Set:
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def contains(self, n):
        curr = self.head
        while True:
            if curr.val == n:
                return True

            if curr.next is not None:
                curr = curr.next
            else:
                return False

    def put(self, n):
        if not self.contains(n):
            self.tail.next = Node()
            self.tail = self.tail.next
            self.tail.val = n

    def remove(self, n):
        if self.head.next is None:
            return self.head.val == n

        prev = self.head
        curr = self.head.next
        while True:
            if curr.val == n:
                prev.next = curr.next

            if curr.next is not None:
                prev = curr
                curr = curr.next
            else:
                break

    def print(self):
        if self.head.next is not None:
            curr = self.head.next
            while True:
                print(curr.val, end=' ')
                if curr.next is not None:
                    curr = curr.next
                else:
                    print()
                    break


set_ = Set()
set_.put(1)
set_.print()
set_.put(9)
set_.print()
set_.remove(1)
set_.print()
