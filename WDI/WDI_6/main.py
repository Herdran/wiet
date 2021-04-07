# tab = [1, 2, 3, 4, 5, 6]
#
# def func(tab, i=0):
#     number = tab[i]
#     if i < len(tab)-1:
#         func(tab, i+1)
#     tab[len(tab)-i-1] = number
#
# func(tab)
# print(tab)


def transform(x, y, remaining_moves=7, result=""):
    if x == y:
        print(result)
        return True
    elif remaining_moves > 0:
        if transform(x * 3, y, remaining_moves - 1, result+"B"):
            return True
        if x > 9:
            if transform(int(x - x % 100 + (x % 10 * 10) + (x % 100 - x % 10) / 10), y, remaining_moves - 1, result+"A"):
                return True
            n = 10
            while x >= n:
                n *= 10
            n //= 10
            if transform((int(x - (x - x % (n)))), y, remaining_moves - 1, result + "C"):
                return True
        return False


        # for i in range(3):
        #     if i == 0 and x > 9:
        #         return transform(int(x - x % 100 + (x % 10 * 10) + (x % 100 - x % 10) / 10), y, remaining_moves - 1, result+"A")
        #     if i == 1:
        #         return transform(x * 3, y, remaining_moves - 1, result+"B")
        #     if i == 2 and x > 9:
        #         n = 10
        #         while x >= n:
        #             n *= 10
        #         n //= 10
        #         return transform((int(x - (x - x % (n)))), y, remaining_moves - 1, result+"C")



if __name__ == '__main__':
    print(transform(6, 3))
