import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

employee = list(map(int, input().split()))

successor_li = [[] for _ in range(n+1)]
praise_score = [0] * (n+1)

def dfs(start):
    if successor_li[start]:

        for k in successor_li[start]:
            praise_score[k] += praise_score[start]
            dfs(k)

for i in range(1, n+1):
    if employee[i-1] != -1:
        successor_li[employee[i-1]].append(i)

for _ in range(m):
    employee_num, score = map(int, input().split())
    praise_score[employee_num] += score

dfs(1)

for num in range(1, n+1):
    print(praise_score[num], end=' ')
