class Node:
    def __init__(self):
        self.val = None
        self.next = None


class AlmostEmptyList:
    def __init__(self, n=0):
        self.head = Node()
        curr = self.head
        for i in range(n):
            curr.next = Node()
            curr = curr.next
        self.tail = curr

    def get(self, id_):
        curr = self.head
        for i in range(n+2):
            if curr.next


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


ael = AlmostEmptyList(10)
ael.print()
