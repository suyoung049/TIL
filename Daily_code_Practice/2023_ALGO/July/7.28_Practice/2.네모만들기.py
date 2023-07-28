import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

answer = 0
for num in range(1, n+1):
    square = set()
    for i in range(1, num+1):
        if i in square:
            continue
        if num % i == 0:
            square.add(i)
            square.add(num//i)
            answer += 1

print(answer)
