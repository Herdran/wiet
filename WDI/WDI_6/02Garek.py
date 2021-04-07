def cw_02(t):
    def number_weight(n):
        weight = 0
        i = 2
        while n > 1:
            add_weight = False
            while n % i == 0:
                n //= i
                add_weight = True
            if add_weight:
                weight += 1
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


    t2 = [0]*(len(t))
    for i in range(len(t)):
        t2[i] = number_weight(t[i])
    if sum(t2) % 3 != 0:
        return False
    return sums(t2)


t = [64, 6, 30, 30]
print(cw_02(t))
# print(t)
