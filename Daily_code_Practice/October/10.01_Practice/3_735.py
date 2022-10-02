import sys
import itertools
sys.stdin = open('3_input.txt', 'r')

T = int(input())


for test_case in range(1, T+1):
    
    num_list = list(map(int, input().split()))
    big = []

    for j in itertools.combinations(num_list, 3):
        if sum(j) not in big:
            big.append(sum(j))
    
    big.sort()
    print(f'#{test_case} {big[-5]}')
        
        

        


