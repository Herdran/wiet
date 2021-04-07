n = 9
# list_ = [1, 2, 3, 1, 5, 2, 2, 2, 6]
list_ = [1, 1, 5, -4, 5, 2, -6, 2, -1]
sum1_ = 0
sum2_ = 0
amount = 1
final_amount = 1
for i in range(n - 1):
    sum1_ += list_[i]
    sum2_ = 0
    for j in range(i + 1, n):
        sum2_ += list_[j]
        if sum2_ == sum1_:
            amount += 1
            sum2_ = 0
        if sum2_ > sum1_ and j == n - 1:
            amount = 1
            break
        if amount > final_amount and j == n - 1:
            final_amount = amount
            amount = 1
print(final_amount)
