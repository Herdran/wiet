def number_weight(n):
    weight = 0
    i = 2
    add_weight = False
    while n > 1:
        while n % i == 0:
            n //= i
            add_weight = True
        if add_weight == True:
            weight += 1
            add_weight = False
        i += 1
    return weight


def sums(arr, index=0, sum1=0, sum2=0, sum3=0):
    if index == len(arr):
        if sum1 == sum2 == sum3:
            return True
    else:
        val = arr[index]
        return sums(arr, index + 1, sum1 + val, sum2, sum3) or \
               sums(arr, index + 1, sum1, sum2 + val, sum3) or \
               sums(arr, index + 1, sum1, sum2, sum3 + val)
        # return x or y or z
    return False


if __name__ == '__main__':
    list_ = [64, 6, 30, 30]
    for i in range(len(list_)):
        list_[i] = number_weight(list_[i])
    print(sums(list_))
