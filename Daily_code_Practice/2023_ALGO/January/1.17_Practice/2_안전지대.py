def pprint(list_):
    for row in list_:
        print(row)
borad = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]

check = [[False] * len(borad) for _ in range(len(borad))]


dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, -1, 1, -1, 1]

for j in range(len(borad)):
    for k in range(len(borad)):

        if borad[j][k] == 1 and check[j][k] == False:

            for i in range(8):

                ny = j + dy[i]
                nx = k + dx[i]

                if 0<= ny < len(borad) and 0<= nx < len(borad):
                    if borad[ny][nx] == 0:
                        check[ny][nx] = True
                        borad[ny][nx] = 1

answer = 0

for i in borad:
    answer += i.count(0)

print(answer)