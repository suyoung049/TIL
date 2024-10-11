n = 4
def solution(n):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    matrix = [list(0 for _ in range(n) ) for _ in range(n)]
    start_num = 1
    dir_num = 0
    y, x = 0, 0
    while (start_num <= n** 2):
      if (0 <= y < n and 0<= x < n and matrix[y][x] == 0):
          matrix[y][x] = start_num
          start_num += 1
          y , x = y + direction[dir_num % 4][0], x + direction[dir_num % 4][1]
      else:
         y, x = y - direction[dir_num % 4][0], x - direction[dir_num % 4][1]
         dir_num += 1
         y , x = y + direction[dir_num % 4][0], x + direction[dir_num % 4][1]
         
        
    return matrix

solution(n)