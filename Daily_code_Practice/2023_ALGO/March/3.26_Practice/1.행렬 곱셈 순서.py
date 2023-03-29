import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

procession_list = []

for _ in range(n):
    y, x = map(int, input().split())
    procession_list.append((y,x))

d = []
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    if i == 0:
        d.append(procession_list[i][0])
        d.append(procession_list[i][1])
    
    else:
        d.append(procession_list[i][1])

INF = sys.maxsize
for i in range(1, n+1):
    dp[i][i] = 0
for diagonal in range(1, n):
    for j in range(1, n-diagonal+1):
        answer = INF
        i = j + diagonal
        k = j
        while True:
            answer = min(answer, dp[j][k] + dp[k+1][i] + (d[j-1] * d[k] * d[i]))
            k += 1
            if k == i:
                break
        dp[j][i] = answer

pprint(dp)
print(dp[1][n])
