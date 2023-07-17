from collections import deque
n = 1
info = 	[1,0,0,0,0,0,0,0,0,0,0]

def bfs(n, info):
    win_list = []
    q = deque([(0, [0,0,0,0,0,0,0,0,0,0,0])])
    max_gap = -1

    while q:
        score_idx, score_board = q.popleft()

        if sum(score_board) > n:
            continue

        elif score_idx == 10:
            temp = score_board.copy()
            temp[score_idx] = n - sum(score_board)
            q.append((-1, temp))

        elif sum(score_board) < n:
            temp_plus = score_board.copy()
            temp_plus[score_idx] = info[score_idx] + 1
            q.append((score_idx+1, temp_plus))
            temp_zero = score_board.copy()
            temp_zero[score_idx] = 0
            q.append((score_idx + 1, temp_zero))

        
        elif sum(score_board) == n:
            lion, apeach = 0, 0

            for i in range(11):
                if info[i] == score_board[i] == 0:
                    continue
                elif info[i] >= score_board[i]:
                    apeach += (10 - i)
                else:
                    lion += (10 - i)
            
            if lion > apeach:
                gap = lion - apeach
                if gap >= max_gap:
                    max_gap = gap
                    win_list.append(score_board)
    return win_list


result = bfs(n, info)

if not result:
    print(-1)
else:
    print(result[-1])
