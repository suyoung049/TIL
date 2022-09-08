import sys
sys.stdin = open('2_input.txt', 'r')



T = int(input())

for test_case in range(1, T+1):

    command = list(input())
    a , b = 1, 1

    for i in range(len(command)):
        if command[i] == "L":
            b += a

        elif command[i] == 'R':
            a += b
    print(f'#{test_case}', end = ' ')
    print(a, b)