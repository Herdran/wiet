list1_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2_ = [1, 3, 4, 5, 6, 9, 10, 11, 14]
list3_ = [0] * len(list1_)
sum_of_deleted_elements = 0
for i in range(len(list1_)):
    for j in range(len(list2_)):
        if list1_[i] < list2_[j]:
            break
        if list1_[i] == list2_[j]:
            list3_[i] = list1_[i]
            list1_[i] = 0
            list2_[j] = 0
            sum_of_deleted_elements += 2
            j = len(list2_)
x = 0
for i in range(len(list3_)):
    if list3_[i] == 0:
        x += 1
list_final_ = [0] * (len(list3_) - x)
j = 0
for i in range(len(list3_)):
    if list3_[i] != 0:
        list_final_[j] = list3_[i]
        j += 1
print(list_final_)

# print(sum_of_deleted_elements, list1_, list2_)
