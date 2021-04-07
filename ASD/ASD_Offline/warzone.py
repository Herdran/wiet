def split(word):
    return [char for char in word]


# def check_anagram(A, B, k, n):
#     array = [0 for _ in range(52)]
#     # array = []
#     # i = 0
#     # while k > 0:
#     #     if not array:
#     #         array.append(A[i])
#
#     for i in range(n):
#         # print(array)
#         array[ord(A[i]) - ord("a")] += 1
#         array[ord(B[i]) - ord("a")] -= 1
#     for i in array:
#         if i != 0:
#             return False
#     return True


# def check_anagram(A, B, k, n):
#     array = []
#     i = 0
#     x = k
#     while x > 0 and i < k:
#         if (A[i], 0) not in array:
#             array.append((A[i], 0))
#             x -= 1
#         i += 1
#     if len(array) < k:
#         i = 0
#         x = k
#         while x > 0 and i < k:
#             if (B[i], 0) not in array:
#                 array.append((B[i], 0))
#                 x -= 1
#             i += 1
#
#     for i in range(n):
#         x = 0
#         y = 0
#         while array[x][0] != A[i]:
#             x += 1
#         array[x] = (array[x][0], array[x][1]+1)
#         while array[y][0] != B[i]:
#             y += 1
#         array[y] = (array[y][0], array[y][1]-1)
#     for i in range(k):
#         if array[i][1] != 0:
#             return 0
#     return 1

# A = input("First word: ")
# B = input("Second word: ")

# def is_anagram(word_a: List[int], word_b: List[int], k: int) -> bool:
#     poma = [0] * k
#     pomb = [0] * k
#     for i in range(len(word_a)):
#         poma[word_a[i]] += 1
#     for i in range(len(word_b)):
#         pomb[word_b[i]] += 1
#
#     for i in range(k):
#         if (poma[i] != pomb[i]):
#             return False
#
#     return True

A = "Alab"
B = "bAal"
n = len(A)
k = 4
print(A.list[int])
print(A, split(A), n)
if check_anagram(split(A), split(B), k, n):
    print("Jej")
else:
    print("Nej")


