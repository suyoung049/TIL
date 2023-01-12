import sys
sys.stdin = open('9_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

solution = list(map(int, input().split()))

inf = sys.maxsize

left = 0
right = 0

for i in range(n-1):
    current = solution[i]

    start = i+1
    end = n 

    while True:
        if start > end:
            break

        else:
            mid = (start + end)//2
            sum_ = current + solution[mid]

            if abs(sum_) < inf:
                inf = abs(sum_)
                left = i
                right = mid

                if sum_ == 0:
                    break

            if sum_ < 0:
                start = mid +1

            else:
                end = mid -1

print(solution[left], solution[right])
