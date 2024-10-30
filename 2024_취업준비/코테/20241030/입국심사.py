n = 6
times = [2, 5] 

def solution(n, times):
    answer = 0
    start = 0
    end = 100000000000000000000000000000000000000000000

    while start <= end:
        mid = (start + end) //2

        people = 0
        for time in times:
            people += (mid//time)
        
        if people >= n:
            answer = mid
            end = mid -1
        
        else:
            start = mid + 1

    return answer


print(solution(n, times))