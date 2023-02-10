board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0], [1, 2, 2, 1]]
moves = [2, 3, 1, 4, 2, 3]
check = []

n = len(board)

def pprint(list_):
    for row in list_:
        print(row)

count = 0
for j in moves:
    for i in range(n):
        if board[i][j-1] != 0:
            if len(check) >= 1 and check[-1] == board[i][j-1]:
                count += 1
                check.pop()
            else:
                check.append(board[i][j-1])
            board[i][j-1] = 0
            break
    

print(count*2)          