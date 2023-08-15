import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))
sum_li = [num_li[0]]

for i in range(1, n):
    sum_li.append(sum_li[-1] + num_li[i])


m = int(input())

for _ in range(m):
    start, end = map(int, input().split())
    answer = 0
    if start == end:
        print(num_li[start-1])
    
    elif start == 1:
        print(sum_li[end-1])
    
    else:
        print(sum_li[end-1] - sum_li[start-2])
    
    