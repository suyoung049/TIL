import sys
sys.stdin = open("3_input.txt", "r")
input = sys.stdin.readline

n = int(input())

student_li = list(map(int, input().split()))
answer = []

for k in range(1, n+1):
    answer.append(k)


for i in range(n):
    move, num = student_li[i], answer[i]

    for j in range(i, i-move, -1):
        answer[j] = answer[j-1]
    

    answer[i-move] = num

print(*answer)