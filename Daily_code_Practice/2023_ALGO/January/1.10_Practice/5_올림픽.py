import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
medal = []


for _ in range(n):
    a, b, c, d = map(int, input().split())
    medal.append([a,b,c,d])

sr_medal = sorted(medal, key=lambda x: -x[3])
sr_medal = sorted(sr_medal, key=lambda x: -x[2])
sr_medal = sorted(sr_medal, key=lambda x: -x[1])


for i in range(n):
    if sr_medal[i][0] == m:
        index = i

for i in range(n):
    if sr_medal[index][1:] == sr_medal[i][1:]:
        print(i + 1)
        break

