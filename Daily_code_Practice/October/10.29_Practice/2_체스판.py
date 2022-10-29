import sys
sys.stdin = open('2_input.txt', 'r')

def pprint(list_):
    for row in list_:
        print(row)

T = int(input())

for test_case in range(1, T+1):
    matrix = [list(input().strip()) for _ in range(8)]
    check = True
 


    for j in range(8):
        if (matrix[j].count('O')) != 1:
            check = False
            

    for j in range(8):
        list_ = []
        for i in range(8):
            list_.append(matrix[i][j])

        if (list_.count('O')) != 1:
            check = False
    
    print(f'#{test_case}', end = ' ')
    if check == False:
        print('no')

    else:
        print('yes')
      

    
            




