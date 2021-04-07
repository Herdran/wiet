def sequence_a(n):
    if n == 1:
        return 1
    return sequence_a(n - 1) + (sequence_b(n)/3)

def sequence_b(n):
    if n == 1:
        return 2
    return sequence_b(n - 1) + sequence_a(n - 1)


k = int(input("A number: "))
smaller = 0
bigger = 0
n = 1
while k > bigger:
    smaller = bigger
    bigger = sequence_a(n)
    n += 1
if k - smaller > (k - bigger) * - 1:
    n_a = n - 1
    a = bigger
else:
    n_a = n - 2
    a = smaller
smaller = 0
bigger = 0
n = 1
while k > bigger:
    first = bigger
    bigger = sequence_b(n)
    n += 1
if k - smaller > (k - bigger) * - 1:
    n_b = n - 1
    b = bigger
else:
    n_b = n - 2
    b = smaller
print(a, b)

if a == b:
    if n_a < n_b:
        print(n_a, "Ciąg a")
    else:
        print(n_b, "Ciąg b")
else:
    if abs(k - a) < abs(k - b):
        print(n_a, "Ciąg a")
    else:
        print(n_b, "Ciąg b")