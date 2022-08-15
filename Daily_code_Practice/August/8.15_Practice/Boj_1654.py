import sys

sys.stdin = open("1654_input.txt", "r")

N, M = map(int, input().split())
lan = []
for _ in range(N):
    lan.append(int(input()))

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for num_ in lan:
        lines += num_ // mid
    
    if lines >= M:
        start = mid + 1

    else:
        end = mid - 1
print(end)
    