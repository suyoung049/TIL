import sys

sys.stdin = open("42_input.txt", "r")

dr = [0, 1, 1]
dc = [1, 1, 0]

buliding = '#'
car = 'X'
void = '.'

R, C = list(map(int, input().split()))
matrix = []
for _ in range(R):
    list_ = list(input())
    matrix.append(list_)
break_count_list = [0] * 5

for r in range(R):
    for c in range(C):
        break_count = 0

        # if matrix[r][c] == buliding:
        #     continue
         # 성립이 안되는 조건들은 continue로 지나가고,
         # 조건이 성립될 때만 정상적인 코드를 실행한다.

        if matrix[r][c] == car:
            break_count += 1
        
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]

            if (-1 < nr < R and -1 < nc < C):
                

                if matrix[nr][nc] == car:
                    break_count += 1
        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)