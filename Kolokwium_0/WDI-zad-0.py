N = 30000
factorial = 1
for i in range(1, N + 1):
    factorial *= i
    while factorial % 10 == 0:
        factorial //= 10
    # print(factorial)
    # factorial = factorial % 100
    # print(factorial)
print(factorial % 10)

n = 15
x = 1
for i in range(2, n + 1):
    if i % 10 != 0:
        x = x * (i % 100)
        while x % 10 == 0:
            x = x // 10
        x = x % 100
print(x % 10)
