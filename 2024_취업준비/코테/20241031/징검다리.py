distance, rocks, n = 25, [2, 14, 11, 21, 17], 2

def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()

    while start <= end:
        stone_cnt = 0
        stone_start = 0

        mid = (start + end) // 2

        for rock in rocks:
            if rock - stone_start < mid:
                stone_cnt += 1
            else:
                stone_start = rock
        
        if n < stone_cnt:
            end = mid -1
        else:
            answer = mid
            start = mid + 1


    return answer


print(solution(distance, rocks, n))