from collections import deque
n = 5
info = 	[2,1,1,1,0,0,0,0,0,0,0] 

def bfs(n, info):
    info_2 = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    max_gap = -1

    while q:
        coun_, arrow = q.popleft()

        if sum(arrow) == n:
            apeach, lion = 0, 0

            for idx in range(11):
                if info[idx] == arrow[idx] == 0:
                    continue
                elif info[idx] >= arrow[idx]:
                    apeach += 10 - idx

                else:
                    lion += 10 -idx
            
            if lion > apeach:
                gap = lion - apeach
                if gap >= max_gap:
                    max_gap = gap
                    info_2.clear()
                    info_2.append(arrow)
        
        elif sum(arrow) > n:
            continue

        elif coun_ == 10:
            temp = arrow.copy()
            temp[coun_] = n - sum(arrow)
            q.append((-1, temp))

        else:
            temp = arrow.copy()
            temp[coun_] = info[coun_] + 1
            q.append((coun_ + 1, temp))
            temp_2 = arrow.copy()
            temp_2[coun_] = 0
            q.append((coun_ + 1, temp_2))
    
    return info_2

win_list = bfs(n, info)

if not win_list:
    print([-1])
else:
    print(win_list)