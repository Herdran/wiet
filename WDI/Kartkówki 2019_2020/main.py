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

numbers = [1] * 1000
print(binary_to_decimal(numbers))