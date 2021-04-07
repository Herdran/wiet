x = 1
y = 1
sum_ = 1
while x < 100:
    for i in range(x):
        y = (i+1)*y
    sum_ = sum_ + 1/y
    x += 1
    y = 1
print(sum_)
