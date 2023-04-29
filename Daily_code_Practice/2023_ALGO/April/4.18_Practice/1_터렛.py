import sys
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1-x2)**2 +(y1-y2)**2) **0.5

    if x1==x2 and y1==y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if r1 > r2:
            if r1-r2 > d:
                print(0)
            elif r1-r2 == d:
                print(1)
            elif r1-r2 < d < r1+r2:
                print(2)
            elif r1 + r2 == d:
                print(1)
            elif r1 + r2 < d:
                print(0)
        elif r2 > r1:
            if r2 - r1 > d:
                print(0)
            elif r2 - r1 == d:
                print(1)
            elif r2-r1 < d < r2 + r1:
                print(2)
            elif r2 + r1 == d:
                print(1)
            elif r2 + r1 < d:
                print(0)
        
        else:
            if r1 + r2 == d:
                print(1)
            elif r1 + r2 < d:
                print(0)
            elif r1 + r2 > d:
                print(2)