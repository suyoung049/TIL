import sys
sys.stdin = open('2_input.txt', 'r')
from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
    n, cal = map(int, input().split())

    ham = []

    for _ in range(n):
        a = list(map(int, input().split()))
        ham.append(a)
        
    result = 0
    for i in range(1, n+1):
        for chi in combinations(ham, i):
            cost = 0
            ca = 0
            for j in chi:
                ca += (j[1])
                cost += (j[0])

                if ca <= cal:
                    result = max(result, cost)
                
    print(f'#{test_case} {result}')