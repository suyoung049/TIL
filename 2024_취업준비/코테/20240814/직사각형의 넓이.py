dots = [[1, 1], [2, 1], [2, 2], [1, 2]]
def solution(dots):
    answer = 0
    len_x = 0
    len_y = 0
    for i in range(len(dots) - 1):
        for j in range(i+1, len(dots)):
            if (abs(dots[i][0] - dots[j][0]) != 0):
                len_x = abs(dots[i][0] - dots[j][0])
            
            if (abs(dots[i][1] - dots[j][1]) != 0):
                len_y= abs(dots[i][1] - dots[j][1])
   
          
    return len_x * len_y

solution(dots)