import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())

num_li = list(map(int, input().split()))

num_sum = 0


for i in range(m):
    num_sum += num_li[i]

max_visit = num_sum
length_cnt = 1

for j in range(m, n):
    num_sum = num_sum + num_li[j] - num_li[j-m]
    if max_visit < num_sum:
        max_visit = num_sum
        length_cnt = 1
    elif max_visit == num_sum:
        length_cnt += 1

if not max_visit:
    print("SAD")
else:
    print(max_visit)
    print(length_cnt)