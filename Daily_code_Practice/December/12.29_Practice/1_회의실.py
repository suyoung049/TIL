import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


n = int(input())

table = []

for _ in range(n):
    y, x = map(int, input().split())

    table.append([y,x])

# 뒤에 있는거 먼저 정렬하는거 기억
last = sorted(table, key=lambda x:(x[1], x[0]))
print(last)

coun = 1

end = last[0][1]

for i in range(1,n):
    if last[i][0] >= end:
        coun += 1
        end = last[i][1]
print(coun)