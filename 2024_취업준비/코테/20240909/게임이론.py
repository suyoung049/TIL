board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = 	[1, 0]
bloc = 	[1, 2]

def solution(board, aloc, bloc):
    answer = -1
    win, depth = search(board, aloc, bloc, 0)
    return depth

# 반드시 이길 사람을 구하는 함수 입니다.
def search(board, aloc, bloc, turn):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = 0, 0
    #turn이 짝수라면 a턴, turn이 홀수 라면 b 턴
    if turn % 2 == 0:
        y, x = aloc[0], aloc[1]
    else:
        y, x = bloc[0], bloc[1]

    #다음으로 움직일 좌표 정리
    nloc = []
    for i in range(4):
        if 0<= y + dy[i] < len(board) and 0<= x + dx[i] < len(board[0]):
            if board[y+dy[i]][x+dx[i]] == 1:
                nloc.append([y + dy[i], x + dx[i]])
    
    # 다음 이동 경로가 없을 경우 현재 턴의  현재 플레이어 패배
    if not nloc:
        return False, 0
    # 다음 이동 경로가 존재하는데, A와 B의 좌표가 같다면 다음 턴에 현재플레이어 승리
    elif aloc == bloc:
        return True, 1
    
    # 승리 가능성 구하는 dfs
    canWin = False
    minTurn, maxTurn = len(board) * len(board[0]) , 0

    for move in nloc:
        # 이동 했으니 이동한 칸은 발판 제거
        board[y][x] = 0
        # A턴일 경우 다음 턴은 B
        if turn % 2 == 0:
            result, cnt = search(board, move, bloc, turn + 1)
        # B턴일 경우 다음 턴은 A
        else:
            result, cnt = search(board, aloc, move, turn + 1)
        # 백트래킹
        board[y][x] = 1

        # 다음 턴의 결과가 지는 경우라면 현재턴의 플레이어가 무조건 승리하는 플레이어(게임이론)
        if not result:
            canWin = True
            minTurn = min(minTurn, cnt + 1)
        
        # 그러나 다음 턴의 결과가 이기는 경우라고 해서 현재턴의 플레이거가 무조건 패배하는 플레이어는 아니다.
        elif not canWin:
            maxTurn = max(maxTurn, cnt + 1)
        
    # 지금 depth에서 승리하는 경우라면 무조건 최소한의 이동 수를 반환
    if canWin:
        depth = minTurn
    # 반대로 질 수 있는 경우라면 최대한의 이동수를 반환
    else:
        depth = maxTurn
    return canWin, depth

solution(board, aloc, bloc)

