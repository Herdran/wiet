# def place_digits(index=1):
#     if index == 9:
#         print(list_)
#     else:
#         for i in range(2, 10):
#             if i not in list_:
#                 if i in primes and list_[index-1] not in primes or i not in primes:
#                     if abs(list_[index-1] - i) >=2:
#                         list_[index] = i
#                         place_digits(index+1)
#                         list_[index] = 0
#
# list_ = [0]*9
# list_[0] = 1
# list2_ = [0]
# primes = [2, 3, 5, 7]
# place_digits()


# Jakub Radek, założyłem tutaj, że odległość między wierszami które ze sobą graniczą wynosi 0
def binary_to_decimal(numbers):
    x = 2
    y = 0
    decimal_value = 0
    length = len(numbers)
    for i in range(len(numbers)):
        decimal_value += numbers[length - i - 1]*(x**y)
        y += 1
    #end for
    return decimal_value
#end def


def distance(T):
    length = len(T)
    list_ = [0] * length
    for i in range(len(T)):
        list_[i] = binary_to_decimal(T[i])
    # end for
    max = 0
    max_indx = 0
    min = 999999999
    min_indx = 0
    for i in range(length):
        if list_[i] > max:
            max = list_[i]
            max_indx = i
        #end if
        if list_[i] < min:
            min = list_[i]
            min_indx = i
        #end if
    #end for
    return abs(max_indx - min_indx) - 1
#end def

T = [[0, 0, 1], [0, 1, 1], [1, 1, 1]]

print(distance(T))