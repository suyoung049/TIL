from copy import deepcopy
from heapq import heappop, heappush
k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
comb_lis = []

# 2번 각 유형의 쉬는 시간을 구하는 함수
def count_rest_time(req_dict, comb):
    total_time = 0
    for key in req_dict:
        rest_time = 0
        task_list = []
        possible = comb[key - 1]
        for task in req_dict[key]:
            if len(task_list) < possible:
                task_time = task[0] + task[1]
                heappush(task_list, task_time)
            else:
                complete = heappop(task_list)
                wait_time = max(0, complete - task[0])  # 대기 시간은 음수가 될 수 없습니다.
                rest_time += wait_time
                start_time = max(complete, task[0])  # 상담 시작 시각은 멘토와 참가자 중 늦은 시각입니다.
                task_time = start_time + task[1]
                heappush(task_list, task_time)
        total_time += rest_time
    return total_time

# 멘토를 할당하는 경우의 모든 조합 구하기
def make_comb(comb, k, n, num_sum):
    global comb_lis
    if len(comb) == k:
        if num_sum == n:
            comb_lis.append(comb)
            return
        else:
            return

    for i in range(1, n-k+2):
        copy_comb = deepcopy(comb)
        copy_comb.append(i)
        num_sum += i
        make_comb(copy_comb, k, n, num_sum)
        num_sum -= i
        

def solution(k, n, reqs):
    global comb_lis
    req_dict = dict()
    for s, e, t in reqs:
        if t in req_dict:
            req_dict[t].append((s,e))
        else:
            req_dict[t] = [(s,e)]

    for i in range(1, n-k+2):
        make_comb([i], k, n, i)
    
    print(comb_lis)

    min_time = float('inf')
    for comb in comb_lis:
        result = count_rest_time(req_dict, comb)
        min_time = min(min_time, result)

    return min_time


print(solution(k, n, reqs))