# Jakub Radek
# Program ten dla każdego elementu listy sprawdza k elementów do przodu, jeśli napotka mniejszy od sprawdzanego, to zamienia
# je miejscami, następnie ponownie zaczyna sprawdzanie od tego miejsca aż nie dojdzie do końca listy
# Szacowana złożoność tego algorytmu to nlogn


from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 



def SortH(p,k):
    curr_sorted = p
    curr = p
    prev = None
    prev_sorted = None
    sorted = False
    while curr_sorted:
        i = 0
        curr = curr_sorted
        while i < k and curr:
            if curr.val == curr_sorted.val:
                i -= 1
                pass
            else:
                if curr.val < curr_sorted.val:
                    if curr_sorted.val == p.val:
                        tmp = curr.next
                        if curr_sorted.next.val == curr.val:
                            curr.next = curr_sorted
                            prev_sorted.next = curr
                            curr_sorted.next = tmp
                        else:
                            curr.next = curr_sorted.next
                            prev.next = curr_sorted
                            curr_sorted.next = tmp
                        p = curr
                        if prev_sorted:
                            prev_sorted.next = curr
                    else:
                        tmp = curr.next
                        if curr_sorted.next.val == curr.val:
                            curr.next = curr_sorted
                            prev_sorted.next = curr
                            curr_sorted.next = tmp
                        else:
                            curr.next = curr_sorted.next
                            prev.next = curr_sorted
                            curr_sorted.next = tmp
                        if prev_sorted:
                            prev_sorted.next = curr
                    sorted = True
            if sorted:
                sorted = False
                curr_sorted = curr
                i = 0
            else:
                i += 1
                prev = curr
                curr = curr.next
        prev_sorted = curr_sorted
        if curr_sorted:
            curr_sorted = curr_sorted.next
    return p


runtests( SortH )