import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

up_cnt = [0] * (m+1)
down_cnt = [0] * (m+1)
min_hight = n
length_cnt = 0

for i in range(n):
    if i % 2 == 0:
        down_cnt[int(input())] += 1
    else:
        up_cnt[int(input())] += 1

for i in range(m-1, 0 , -1):
    up_cnt[i] += up_cnt[i+1]
    down_cnt[i] += down_cnt[i+1]


for j in range(1, m+1):
    if min_hight > down_cnt[j] + up_cnt[m-j + 1]:
        min_hight = down_cnt[j] + up_cnt[m-j + 1]
        length_cnt = 1
    elif min_hight == down_cnt[j] + up_cnt[m-j + 1]:
        length_cnt += 1 

print(min_hight, length_cnt)