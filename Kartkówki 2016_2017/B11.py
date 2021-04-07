def sequence_a(n):
    if n == 1 or n == 2:
        return 1
    return sequence_a(n - 1) + (sequence_a(n - 2))


def sequence_b(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    return sequence_b(n - 1) + sequence_b(n - 2) + sequence_b(n - 3)

def sequence_c(n):
    list_ = [0]*n*4
    for i in range(2 * n):
        list_[i] = sequence_a(i + 1)
        list_[i + 2 * n] = sequence_b(i + 1)
    for j in range(n*4 - 1):
        for i in range(n*4 - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    x = 1
    for i in range(n*4 - 1):
        if list_[i] != list_[i+1]:
            x += 1
        if x - 1 == n:
            return (list_[i])

k = int(input("A number: "))

print(sequence_c(k))

