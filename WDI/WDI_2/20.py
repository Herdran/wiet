# def into_different_zapisy(number, numeral_system):
#     list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
#     print(number)
#     list1_ = [0] * (number // numeral_system + 1)
#     i = 0
#     length = 0
#     while number > 0:
#         list1_[i] = (list_[number % numeral_system])
#         number //= numeral_system
#         i += 1
#         length += 1
#
#     number = [0] * length
#     i = 0
#     while length > 0:
#         number[i] = list1_[length - 1]
#         i += 1
#         length -= 1
#
#     return number
def number_to_n_sys(num, k):
    cnt = 1
    while num >= k ** cnt:
        cnt += 1
    result = [None for _ in range(cnt)]
    index = cnt - 1
    while num != 0:
        result[index] = num % k
        num //= k
        index -= 1
    return result


print(number_to_n_sys(10, 12))
