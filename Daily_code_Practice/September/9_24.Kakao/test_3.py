commands = ['UPDATE 1 1 menue', 'UPDATE 1 2 category',
            'UPDATE 2 1 bibimbap', 'UPDATE 2 2 korean',
            'UPDATE 2 3 rice', 'UPDATE 3 1 ramyeon',
            'UPDATE 3 2 korean', 'UPDATE 3 3 nondle',
            'UPDATE 3 4 instant', 'UPDATE 4 1 pasta',
            'UPDATE 4 2 italian', 'UPDATE 4 3 noodle',
            'MERGE 1 2 1 3','MERGE 1 3 1 4', 'UPDATE korean hansik',
            'UPDATE 1 3 group','UNMERGE 1 4', 'PRINT 1 3', 'PRINT 1 4']

matrix = [[0] * 10 for _ in range(10)]
marge = [[0] * 10 for _ in range(10)]

def pprint(list_):
    for row in list_:
        print(row)

for command in commands:
    command = command.split()
    
    if command[0] == 'UPDATE':
        if len(command) == 4:
            y, x = int(command[1]), int(command[2])
            if marge[y][x] != 0:
                for j in range(10):
                    for i in range(10):
                        if marge[j][i] != 0:
                            matrix[j][i] = command[3]
            else:
                matrix[y][x] = command[3]
        else:
            for j in range(10):
                for i in range(10):
                    if matrix[j][i] == command[1]:
                        matrix[j][i] = command[2]
    
    if command[0] == 'MERGE':
        y1, x1, y2, x2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        marge[y1][x1] = matrix[y1][x1]
        marge[y2][x2] = matrix[y1][x1]
        matrix[y2][x2] = matrix[y1][x1]


    if command[0] == 'UNMERGE':
        y, x = int(command[1]), int(command[2])
        
            


