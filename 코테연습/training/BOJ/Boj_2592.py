import sys

sys.stdin = open("2592_input.txt", "r")
num_list = []

for _ in range(10):
    num_list.append(int(input()))
a = sum(num_list) // len(num_list)
print(a)

num_dic = dict()
for i in range(len(num_list)):
    if num_list[i] in num_dic:
        num_dic[num_list[i]] += 1
    else:
        num_dic[num_list[i]] = 1
max = 0
for i in num_dic:
    if num_dic[i] > max:
        max = num_dic[i]
        b = i
print(b)    