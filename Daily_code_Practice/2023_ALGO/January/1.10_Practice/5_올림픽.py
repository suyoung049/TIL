import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
medal = []


for _ in range(n):
    a, b, c, d = map(int, input().split())
    medal.append([a,b,c,d])


# sr_medal.sort(key=lambda x : (-x[1], -x[2], -x[3]))

sr_medal = sorted(medal, key=lambda x: -x[3])
sr_medal = sorted(sr_medal, key=lambda x: -x[2])
sr_medal = sorted(sr_medal, key=lambda x: -x[1])


print(sr_medal)
for i in range(n):
    if sr_medal[i][0] == m:
        index = i

# 메달 순으로 정렬 하였을 때, 메달 수 같다면 가장앞에있는 나라의 인덱스와 같다. 
for i in range(n):
    if sr_medal[index][1:] == sr_medal[i][1:]:
        print(i + 1)
        break

