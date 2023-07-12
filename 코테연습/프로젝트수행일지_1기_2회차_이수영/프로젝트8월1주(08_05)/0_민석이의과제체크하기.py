import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())

for test_case in range(1, T+1):
   
    student = []
    N, K = map(int, input().split())
    sub = list(map(int, input().split()))
    N_pass = []
    print(f'#{test_case}', end = ' ')
    for i in range(1, N+1):
        student.append(i)
    for i in student:
        if i not in sub:
            N_pass.append(i)
    print(*N_pass)

        
            