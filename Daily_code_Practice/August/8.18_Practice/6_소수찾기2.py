import sys
sys.stdin = open("6_input.txt", "r")
N = int(input())

num_list = list(map(int, input().split()))
coun = []
for num_ in num_list:
    if num_ == 1:
        continue
    for j in range(2, int(num_**0.5) +1):
        if num_%j == 0:
            break
    else:
        coun.append(num_)
print(len(coun))

