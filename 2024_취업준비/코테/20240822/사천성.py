m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def solution(m, n, board):
    dy = [0 , 1, 1]
    dx = [1, 0, 1]
    matrix = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i].append(board[i][j])
    
    stone_count = 0
    while True:
      print(matrix)
      break_stone = set()
      for i in range(m):
          for j in range(n):
              stone = matrix[i][j]
              count = 0
              if stone == '@':
                  continue
              for k in range(3):
                  if 0 <= i + dy[k] < m and 0<= j+dx[k] < n and stone == matrix[i+dy[k]][j+dx[k]] :
                      count += 1
                  
              if count == 3:
                  break_stone.add((i,j))
                  for k in range(3):
                      break_stone.add((i+dy[k], j+dx[k]))
      
      cnt = len(break_stone)
      stone_count += cnt
      for key in break_stone:
          matrix[key[0]][key[1]] = "@"

      for j in range(n):
          for i in range(m-1, -1, -1):
              while i < m:
                  if i == m-1:
                      i += 1
                      continue
                  else:
                      if matrix[i+1][j] == "@":
                          matrix[i+1][j] = matrix[i][j]
                          matrix[i][j] = "@"
                      
                      i += 1
      if cnt == 0:
          break

    return stone_count



print(solution(m, n, board))