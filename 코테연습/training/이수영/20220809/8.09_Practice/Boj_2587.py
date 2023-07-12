import sys

sys.stdin = open("2587_input.txt", "r")

num_list = []

for _ in range(5):
    num_list.append(int(input()))
sum_ = sum(num_list)

a = sum_//len(num_list)

sr_list = sorted(num_list)
for i in range(len(sr_list)):
    b = sr_list[2]
print(a)
print(b)