import sys
sys.stdin = open('2_input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    n, m = input().split()

    n = int(n)
    m = list()
    

    i = 0

    while i < n-1:
        if m[i] == m[i+1]:
            m.pop(i)
            m.pop(i)
            i = 0
            n = n-2
        else:
            i +=1
    
    print(f'#{test_case}', end = ' ')
    print(''.join(m))


    