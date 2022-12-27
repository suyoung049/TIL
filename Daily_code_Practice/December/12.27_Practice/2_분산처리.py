import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a,b = map(int, input().split())
    aa = a%10 # 10대의 컴퓨터에서 10의 나머지는 항상 같다

    if aa == 0:      # 나머지가 0이라면 10번 컴퓨터
        print(10)

    elif aa in [1,5,6]:   # 1,5,6은 어떤수를 제곱해도 본인 자신 
        print(aa)
    
    elif aa in [4,9]:   # 4,9는 제곱수에 따라 나머지가 달라지는데 0일 경우만 2로 따로 처리
        bb = b%2
        if bb == 0:
            print(aa**2%10)
        
        else:
            print(aa**bb%10)

    else:
        bb = b%4                # 2,3,7,8,은 4가지 수로 0일경우만 4로 따로 처리 
        if bb == 0:
            print(aa**4%10)
        else:
            print(aa**bb%10)