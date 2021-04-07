import itertools


list____ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list_ = list(itertools.permutations(list____, 10))
i = 0
print(len(list_))
# n = len(list_)
# while i < n:
#     if list_[i][0] == 0:
#         list_.pop(i)
#         i -= 1
#         n -= 1
#     i += 1
#     print(i, n)

# print(len(list_))
