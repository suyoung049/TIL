
import sys

sys.stdin = open("1_input.txt", "r")

N = int(input())
time = []
for i in range(N):
    data = list(map(int, input().split()))
    time.append(data)
time.sort()
print(time)

last_time = 2**32

# print(time)
cnt = 1
for t in time:
    # print(t, last_time)
    if last_time <= t[0]:
        last_time = t[1]
        cnt += 1
    if last_time > t[1]:
        last_time = t[1]
print(cnt)