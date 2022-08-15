import sys

sys.stdin = open("2751_input.txt", "r")

T = int(input())
num_list = []

for _ in range(T):
    num_list.append(int(input()))
num_list = set(num_list)
sr_num_list = sorted(num_list)
for i in sr_num_list:
    print(i)
