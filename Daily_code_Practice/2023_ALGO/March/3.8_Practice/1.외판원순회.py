import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]


rs = sys.maxsize
def TSP(start, middle, cost, visit):
    global rs
    if len(visit) == n:
        if matrix[middle][start]:
            rs = min(rs, cost + matrix[middle][start])
        return
    
    for j in range(n):
        if middle == j:
            continue
        if matrix[middle][j] and j not in visit and rs > cost:
            visit.append(j)
            TSP(start, j, cost + matrix[middle][j], visit)
            visit.pop()

for i in range(n):
    TSP(i, i, 0, [i])

print(rs)