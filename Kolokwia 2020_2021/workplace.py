# from random import randint
# from random import seed
#
# def prime(n):
#     if n == 2 or n == 3:
#         return True
#     if n < 2 or n % 2 == 0 or n % 3 == 0:
#         return False
#
#     a = 5
#     while a <= (n)**1/2:
#         if n % a == 0:
#             return False
#         a += 2
#         if n % a == 0:
#             return False
#         a += 4
#     return True
#
#
# def horse_check_prime():
#     def horse_check(curr_x, curr_y):
#         for vector in vectors:
#             x = curr_x + vector[0]
#             y = curr_y + vector[1]
#             if 0 <= x < N and 0 <= y < N:
#                 if prime(T[curr_x][curr_y] + T[x][y]):
#                     list2_[0] = True
#
#     vectors = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
#     for i in range(N):
#         for j in range(N):
#             horse_check(i, j)
#
#     if list2_[0] == True:
#         return True
#     return False
#
#
# N = 1000
# seed(2137)
# list2_ = [False]
# rr = (1, 10)
# # T = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# T = [[randint(rr[0], rr[1]) for _ in range(N)] for _ in range(N)]
# print(horse_check_prime())


a, b = (1,2)

print(a)