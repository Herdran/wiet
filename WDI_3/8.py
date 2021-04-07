import random
def if_prime_number(z):
    n = 500
    x = 0
    j = 0
    list_ =[i for i in range(2, n+1)]
    while j <= len(list_):
        for i in range(j+1, len(list_)):
            if list_[i] % list_[j] == 0:
                list_[i] = 0
        x = list_.count(0)
        for i in range(x):
            list_.remove(0)
        j += 1
    i = 0
    while list_[i] <= z:
        if list_[i] == z:
            return True
        i += 1
    return False

def cw8():
    t = 1000
    list_ = [random.randint(1, 1000) for i in range(t)]
    i = 0
    while i < t:
        number = list_[i]
        while number > 0:
            if if_prime_number(number) == True:
                i += number
                number = 0
            else:
                number -= 1





if __name__ == '__main__':
    # print(cw8())
    # print(if_prime_number(23))
