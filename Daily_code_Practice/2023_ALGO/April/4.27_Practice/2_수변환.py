import sys
sys.stdin = open("2_input.txt", "r")

num_li = input()
one_count = 0
zero_count = 0

len_ = len(num_li)

for i in range(len_):
    if i == 0:
        if num_li[i] == "0":
            zero_count += 1
        else:
            one_count += 1
    else:
        
        if num_li[i] == num_li[i-1]:
            continue
        
        if num_li[i] == "0":
            zero_count += 1
        else:
            one_count += 1



print(min(one_count, zero_count))