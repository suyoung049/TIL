import sys
sys.stdin = open('1_input.txt', 'r')

n = int(input())
num_list = list(map(int, input().split()))
k = int(input())

i = 0
while True:
    if k == 0:
        break
    if (i+k+1) < n:
        slice_list = num_list[i:i + k + 1]
    else:
        slice_list = num_list[i:]
    max_num = max(slice_list)
    for j in range(len(slice_list)):
        if slice_list[j] == max_num:
            for t in range(j+i, i, -1):
                num_list[t], num_list[t-1] = num_list[t-1], num_list[t]
                k -= 1
                if k == 0:
                    break
            break

    if i == n-1:
        break
    
    i += 1
print(*(num_list))

    
