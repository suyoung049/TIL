game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
from collections import deque

def solution(game_board, table):
    answer = 0
    board_dict = dict()
    table_dict = dict()
    length = len(game_board)

    for j in range(length):
        for i in range(length):
            if game_board[j][i] == 0:
                candidate_list, frag_len = bfs((j,i), game_board, length, True)
                if board_dict.__contains__(frag_len):
                    board_dict[frag_len].append(candidate_list)
                else:
                    board_dict[frag_len] = [candidate_list]
            
            if table[j][i] == 1:
                candidate_list, frag_len = bfs((j,i), table, length, False)
                if table_dict.__contains__(frag_len):
                    table_dict[frag_len].append(candidate_list)
                else:
                    table_dict[frag_len] = [candidate_list]
   
  
    for key in board_dict:
        if key not in table_dict:
            continue
        for i in range(len(board_dict[key])):
            flag = False
            for j in range(len(table_dict[key])):
                if table_dict[key][j][-1]:
                    continue
                # 마지막은 사용 확인을 플래그이므로 제외
                for fragment in table_dict[key][j][:-1]:
                    if flag:
                        continue
                    check = 0
                    for y, x in board_dict[key][i]:
                        for t_y , t_x in fragment:
                            if y == t_y and x == t_x:
                                check += 1
                    if check ==  key:
                        answer += key
                        table_dict[key][j][-1] = True
                        flag = True
                        continue
    return answer


def bfs(start, game_board, length, check):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    queue = deque([start])
    fragment_set = set([start])

    if check: 
        game_board[start[0]][start[1]] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if check:
                if 0 <= ny < length and 0 <= nx < length and game_board[ny][nx] == 0:
                    fragment_set.add((ny,nx))
                    queue.append((ny,nx))
                    game_board[ny][nx] = 1
            else:
                if 0 <= ny < length and 0 <= nx < length and game_board[ny][nx] == 1:
                    fragment_set.add((ny,nx))
                    queue.append((ny,nx))
                    game_board[ny][nx] = 0


    # 좌표들을 회전 한 후에 정규화 진행하면 범위 벗어나는 문제 해결
    change_90, change_180, change_270 = change_fragment(fragment_set)
    nor_set = make_fragment(fragment_set)
    nor_90 = make_fragment(change_90)
    nor_180 = make_fragment(change_180)
    nor_270 = make_fragment(change_270)
    if check:
        candidate_list = nor_set
    else:
        candidate_list = [nor_180, nor_270, nor_90, nor_set, False]

    return candidate_list, len(nor_set)


def make_fragment(fra_set):
    min_y, min_x = 50, 50
    for y , x in fra_set:
        if min_y > y:
            min_y = y
        if min_x > x:
            min_x = x

    after =  {(y - min_y, x -  min_x) for y, x in fra_set} 
    return after

def change_fragment(fra_set):
    change_90 = set()
    change_180 = set()
    change_270 = set()

    for y, x in fra_set:
        change_90.add((x, -y))
        change_180.add((-y, -x))
        change_270.add((-x, y))

    return change_90, change_180, change_270
print(solution(game_board, table))