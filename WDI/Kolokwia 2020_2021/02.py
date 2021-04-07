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