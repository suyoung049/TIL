from heapq import heappop, heappush
jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    jobs.sort()
    wait = []
    left = -1
    time = jobs[0][0]
    count = 0
    length = len(jobs)

    while count < length:
        for s, t in jobs:
            if left < s <= time:
                heappush(wait, (t,s))
        
        if wait:
            term, start = heappop(wait)
            left = time
            time += term
            count += 1
            answer += (time - start)
        
        else:
            time += 1


    return answer//length

print(solution(jobs))