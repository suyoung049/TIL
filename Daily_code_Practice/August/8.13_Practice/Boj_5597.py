import sys

sys.stdin = open("5597_input.txt", "r")

check_list = [0] * 31

for i in range(28):
    check_list[int(input())] += 1
for i in range(len(check_list)):
    if i == 0:
        continue
    else:
        if check_list[i] == 0:
            print(i)
