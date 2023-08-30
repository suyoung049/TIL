import sys
sys.stdin = open('1_input.txt',"r")
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))
num_li.sort()

sum_li = [num_li[0]]

for i in range(1, n):
    num_sum = sum_li[-1] + num_li[i]
    sum_li.append(num_sum)


for _ in range(m):
    start, end = map(int, input().split())
    if start == 1:
        print(sum_li[end-1])
    else:
        print(sum_li[end-1] - sum_li[start-2])
