# T = int(input())
T = 1
for i in range(T):
    # n = int(input())
    # list1_ = []
    n = 3
    list1_ = [(1, 5), (2, 4), (10, -5)]
    succesful_commands = 0
    for i in range(n):
        t, x = input().split()
        t = int(t)
        x = int(x)
        temp = (t, x)
        list1_.append(temp)
    time = list1_[0][0]
    curr_comm = list1_[0][1]
    position = 0
    passed = False
    moving = False
    command = 0
    while command < n:
        if not moving:
            if list1_[command][0] == time:
                curr_comm = list1_[command][1]
        else:
            if command < n and time == list1_[command+1][0] and position != curr_comm:
                passed = True
                command += 1
            if position == list1_[command][1]:
                succesful_commands += 1
        if position < curr_comm:
            position += 1
            moving = True
        elif position < curr_comm:
            position -= 1
            moving = True
        elif position == curr_comm:
            if not passed:
                succesful_commands += 1
            passed = False
            moving = False
            command += 1
        time += 1

print(succesful_commands)