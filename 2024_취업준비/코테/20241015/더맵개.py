from heapq import heappop, heappush
scovile, k = [1, 2, 3, 9, 10, 12], 7
def solution(scoville, K):
    hot_list = []

    for cnt in scoville:
        heappush(hot_list, cnt)
    
    mix_cnt = 0
    while hot_list:
        spice = heappop(hot_list)
        if spice >= K:
            return mix_cnt
        
        else:
            mix_cnt += 1
            if not hot_list:
                return -1
            second_spice = heappop(hot_list)
            heappush(hot_list, spice + (second_spice * 2))
solution(scovile, k)
