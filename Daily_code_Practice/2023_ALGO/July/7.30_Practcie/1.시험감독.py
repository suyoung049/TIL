import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline


n = int(input())

class_li = list(map(int, input().split()))

b, c = map(int, input().split())

answer = 0
for i in range(n):
    class_li[i] -= b
    answer += 1
    if class_li[i] <= 0:
        class_li[i] = 0

    else:
        if class_li[i] % c != 0:
            answer = answer + (class_li[i] // c) + 1
        else:
            answer = answer + (class_li[i] // c)
print(answer)