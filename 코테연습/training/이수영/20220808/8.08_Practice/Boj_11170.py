import sys

sys.stdin = open("11170_input.txt", "r")
T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    
    coun = 0
    for i in range(N, M+1):
        w = str(i)
        coun += w.count('0')   # list로 맵변환 시키면 1001이 한꺼번에 변환 하나하나 하면 1, 0, 0, 1로 변환
    print(coun)
       
       
        

    
