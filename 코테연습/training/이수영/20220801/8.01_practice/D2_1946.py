import sys

sys.stdin = open("input_1946.txt", "r")
T = int(input())

for test_case in range(1, T +1):
    N = int(input())
    code = ''
    for i in range(N):
        C, K = input().split()
        K = int(K)
        code += C * K
    print(f'#{test_case}')
    for i in range(len(code)):
        if (i+1) % 10 == 0:
            print(code[i])
        else:
            print(code[i], end = '')
    print()
    
