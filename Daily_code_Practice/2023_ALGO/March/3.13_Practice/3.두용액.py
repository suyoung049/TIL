import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
solution_list = list(map(int, input().split()))

solution_list.sort()

left = 0
right = 0

answer = sys.maxsize

for i in range(n-1):
    current_solution = solution_list[i]
    
    start = i + 1
    end = n - 1


    while True:
        if start > end:
            break
        
        mid = (start + end) // 2
 
        solution_sum = current_solution + solution_list[mid]

        if answer >= abs(solution_sum):
            answer = abs(solution_sum)
            left = i
            right = mid

        if solution_sum == 0:
            break

        if solution_sum > 0:
            end = mid -1

        else:
            start = mid + 1

print(solution_list[left], solution_list[right])

