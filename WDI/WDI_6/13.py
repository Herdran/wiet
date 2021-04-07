"""Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2."""

def cw_13(n, p, last=1):
    if n == 0:
        print(p)
    for i in range(last, n + 1):
        cw_13(n-i, p+f'{i} ', i)


n = 4
print(cw_13(n, ''))



# def func(n, p, last):
#   if n == 0:
#     print(p)
#
#   for i in range(last, n+1):
#     func(n-i, p+f'{i} ', i)
#
#
# n = int(input())
# func(n, '', 1)