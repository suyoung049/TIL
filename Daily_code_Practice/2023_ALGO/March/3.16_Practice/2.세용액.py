import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
solution_li = list(map(int, input().split()))
solution_li.sort()


answer = sys.maxsize
for i in range(n-2):
    current = i
    start = i + 1
    end = n-1


    while True:
        if start >= end:
            break

        sum_ = solution_li[start] + solution_li[current] + solution_li[end]

        if answer >= abs(sum_):
            answer = abs(sum_)
            result = [solution_li[start], solution_li[current], solution_li[end]]

            if sum_ == 0:
                break

        if sum_ > 0:
            end -= 1

        else:
            start += 1

result.sort()

print(result)



