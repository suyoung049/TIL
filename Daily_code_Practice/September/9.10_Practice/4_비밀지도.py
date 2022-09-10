number = 2
b = format(number, 'b') 

def pprint(list_):
    for row in list_:
        print(row)


n = 6 
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
x = []
x_2 = []


matrix = [[' ']*n for _ in range(n)]

pprint(matrix)

for i in range(n):
    code = format(arr1[i], 'b')
    
    while len(code) < n:
        code = '0' + code

    x.append(code)

    for j in range(n):
        matrix[i][j] = x[i][j]
# pprint(matrix)

for i in range(n):
    code_2 = format(arr2[i], 'b')

    while len(code_2) < n:
        code_2 = '0' + code_2

    x_2.append(code_2)

    for j in range(n):
        if matrix[i][j] == '0':
            matrix[i][j] = x_2[i][j]    
# pprint(matrix)    

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '0':
            matrix[i][j] = ' '
        else:
            matrix[i][j] = '#'

# pprint(matrix)

answer = []
for i in matrix:
    answer.append(''.join(i))
# print(answer)

    

    
