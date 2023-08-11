import sys
sys.stdin = open('1_input.txt', "r")
input = sys.stdin.readline

n = int(input())

box_li = [0] * 1001
max_high = 0
max_idx = 0
last_idx = 0

for i in range(n):
    idx, high = map(int, input().split())
    box_li[idx] = high
    if idx > last_idx:
        last_idx = idx
    if high >= max_high:
        max_idx = idx
        max_high = high

answer = mx = 0
for i in range(1, max_idx + 1):
    mx = max(mx, box_li[i])
    answer += mx

mx = 0
for j in range(last_idx, max_idx, -1):
    mx = max(mx, box_li[j])
    answer += mx

print(answer)
    

 

