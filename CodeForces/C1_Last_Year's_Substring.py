test_cases = int(input())
for i in range(test_cases):
    length = int(input())
    numbers = input()
    if numbers[0:4] == '2020' or numbers[0:3] + numbers[-1:] == '2020' or numbers[0:2] + numbers[-2:] == '2020' or numbers[0:1] + numbers[-3:] == '2020' or numbers[-4:] == '2020':
        print("YES")
    else:
        print("NO")
