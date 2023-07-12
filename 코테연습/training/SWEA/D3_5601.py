import sys

sys.stdin = open("input_5601.txt", "r")
T = int(input())

for test_case in range(1, T +1):
    N = int(input())

    print(f'#{test_case}', end = " ")
    for i in range(N) :
        print('1/' + str(N), end = ' ')
    print()
        