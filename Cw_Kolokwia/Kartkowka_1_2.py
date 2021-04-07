import random
N = 100
list_ = [random.randint(0, 100) for _ in range(N)]
print(list_)
# list_ = [0, 1, 2, 3, 5, 2, 3, 4, 5, 8]
final_length = 1
for i in range(N):
    sum_of_indexes = i
    sum_of_numbers = list_[i]
    length = 1
    for j in range(i + 1, N):
        if list_[j] > list_[j - 1]:
            sum_of_indexes += j
            sum_of_numbers += list_[j]
            length += 1
        if sum_of_indexes == sum_of_numbers and length > final_length:
            final_length = length
        if list_[j] < list_[j - 1]:
            break
if final_length > 1:
    print(final_length)
else:
    print("Noł")
