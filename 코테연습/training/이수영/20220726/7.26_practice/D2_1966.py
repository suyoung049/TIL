import sys

sys.stdin = open("input_1966.txt", "r")
T = int(input())

for test_case in range(1, T +1):
    N = int(input())

    num = list(map(int, input().split()))

    result = sorted(num)
    print(f'#{test_case}', end = ' ')
    
    for i in range(N):    # N = len(result)
        print(f'{result[i]}', end=' ')
    print()
    
        
      
   
       