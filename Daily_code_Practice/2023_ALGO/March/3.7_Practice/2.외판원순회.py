import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]



answer = sys.maxsize
def recu(start, next, cost, visited):
    global answer
    if len(visited) == n:
        if matrix[next][start]:
            answer = min(answer, cost + matrix[next][start])
        return
    
    for j in range(n):
        if j not in visited and matrix[next][j] and answer > cost:
            visited.append(j)
            recu(start, j, cost + matrix[next][j], visited)
            visited.pop()


for i in range(n):
    recu(i, i, 0, [i])

print(answer)