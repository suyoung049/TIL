a, b, g, s, w, t = 90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]

def solution(a, b, g, s, w, t):
    # 이분 탐색을 시작을 위한 왼쪽 끝, 오른쪽 끝 설정
    # 최대값은 탐색의 최악의 경우 
    l, r = 1, 4 * (10**14)
    length = len(g)
    # 이분 탐색
    while l <= r:
        g_amount, s_amount, w_amount = 0, 0, 0
        T = (l+r) //2
        for i in range(length):
            # 최대 시간보다 편도시간이 클 경우
            if T < t[i]:
                continue
            # 시간에서 옮길수 있는 광물의 최대양 = 편도로 옮기는 광물양 + ((총시간 - 편도 시간) // (편도 시간 * 2)) *  왕복으로 옮길 수 있는 광물의 양
            amount = w[i] + ((T-t[i])//(t[i] * 2)) * w[i]
            # 시간에 따라 옮기는 광물의 양은 한 마을에서 옮길 수 있는 금의 양을 초과 할 수 없다
            g_amount += min(g[i], amount)
            # 은도 역시 마찬가지
            s_amount += min(s[i], amount)
            # 광물의 최대 양 역시 초과 할수 없다
            w_amount += min(g[i] + s[i], amount)
        # 만약 금의 양과, 은의 양, 광물의 총 양을 충분히 넒길 수 있는 시간이 된다면 이분 탐색에서 오른쪽 끝 변경
        if a <= g_amount and b <= s_amount and (a+b) <= w_amount:
            r = T - 1
        # 그렇지 않다면 왼쪽 끝 변경
        else:
            l = T + 1
          
    return l


solution(a, b, g, s, w, t)