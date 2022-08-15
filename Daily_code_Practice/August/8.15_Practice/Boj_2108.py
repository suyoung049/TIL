import sys

sys.stdin = open("2108_input.txt", "r")

T = int(input())
num_list = []

for _ in range(T):
    num_list.append(int(input()))

a = round(sum(num_list) / T)
print(a)
sor_n_list = sorted(num_list)
print(sor_n_list[(T//2)])

n_dict = dict()

for num_ in num_list:
    if num_ in n_dict:
        n_dict[num_] += 1
    else:
        n_dict[num_] = 1
sr_n_dict = sorted(n_dict.items(), key = lambda x : (-x[1], x[0]))

if len(sr_n_dict) > 1:

    if sr_n_dict[0][1] == sr_n_dict[1][1]:
        print(sr_n_dict[1][0])
    else:
        print(sr_n_dict[0][0])
else:
    print(sr_n_dict[0][0])
print(max(num_list) - min(num_list))