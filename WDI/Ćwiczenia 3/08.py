import random
def if_prime_number(z, list_of_primes):
    if z in list_of_primes:
        return True
    else:
        return False


def cw8():
    t = 1000
    list_ = [random.randint(1, 1000) for i in range(t)]
    n = max(list_)
    j = 0
    list_of_primes =[i for i in range(2, n+1)]
    while j <= len(list_of_primes):
        for i in range(j+1, len(list_of_primes)):
            if list_of_primes[i] % list_of_primes[j] == 0:
                list_of_primes[i] = 0
        x = list_of_primes.count(0)
        for i in range(x):
            list_of_primes.remove(0)
        j += 1
    print(list_)
    print("łaaaaaa", list_of_primes)

    i = 0
    while i < t:
        if list_[i] in list_of_primes:

    #     number = list_[i]
    #     while number > 0:
    #         if if_prime_number(number) == True:
    #             i += number
    #             number = 0
    #         else:
    #             number -= 1
# pierdole

if __name__ == '__main__':
    print(cw8())
    # print(if_prime_number(23))
