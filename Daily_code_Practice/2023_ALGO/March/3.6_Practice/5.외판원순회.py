import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


res = sys.maxsize
def TSP(stat, next, cost, visit):
    
    global res
    if len(visit) == n:
        if matrix[next][stat]:
            res = min(res, cost + matrix[next][stat])
        return
    
    for j in range(n):
        if matrix[next][j] != 0 and j not in visit and cost < res:
            visit.append(j)
            TSP(stat, j, cost + matrix[next][j], visit)
            visit.pop()

for i in range(n):
    TSP(i, i, 0, [i])

print(res)




