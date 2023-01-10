import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

solution = list(map(int, input().split()))

answer = sys.maxsize
for i in range(n):
    for j in range(i, n):
        a = abs(solution[i]+solution[j])
        answer = min(answer, a)
