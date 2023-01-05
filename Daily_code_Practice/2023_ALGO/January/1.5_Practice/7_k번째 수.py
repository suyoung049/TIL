array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for y in commands:
    i, j, k = (y[0]-1), (y[1]), (y[2]-1) 

    cut = array[(i):(j)]

    cut = sorted(cut)

    answer.append(cut[k])