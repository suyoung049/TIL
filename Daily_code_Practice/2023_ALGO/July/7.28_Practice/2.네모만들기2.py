import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

answer = 0

for j in range(1, n+1):
    for i in range(j, n+1):
        if j*i <= n:
            answer += 1

print(answer)