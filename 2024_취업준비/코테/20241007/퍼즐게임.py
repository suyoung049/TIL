diffs = [1, 1, 1]
times = [10, 10, 10]
limit = 30

def solution(diffs, times, limit):
    answer = 0
    # level의 최소값을 구하기위한 이분 탐색
    end = 100000
    start = 1

    while(start < end):
        mid = (start + end) // 2
        totalTime = calculate(diffs, times, mid)
        if totalTime > limit:
            start = mid + 1
        else:
            end = mid
    
    return start


def calculate(diffs, times, level):
    length = len(diffs)
    totalTime = 0
    for i in range(length):
        if diffs[i] <= level:
            totalTime += times[i]
        else:
            count = diffs[i] - level
            totalTime += (count * (times[i] + times[i-1])) + times[i]
    
    return totalTime


print(solution(diffs, times, limit))