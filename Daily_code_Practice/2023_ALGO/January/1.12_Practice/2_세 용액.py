import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

solution = list(map(int, input().split()))
solution.sort()
result = sys.maxsize

for i in range(n-2):
    current = solution[i]
    start = i + 1
    end = n - 1

    while True:
        if start >= end:
            break

        sum_ = current + solution[start] + solution[end]

        if abs(sum_) < result:
            result = abs(sum_)
            answer = [solution[start], solution[i], solution[end]]

            if sum_== 0:
                break

        
        if sum_ < 0:
            start += 1

        else:
            end -= 1

answer.sort()

print(answer[0], answer[1], answer[2])