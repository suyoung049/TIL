import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count_ = 0
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    ryu = []
    test = []

    for j in range((x1-r1), (x1+r1)+1):
        for i in range((y1-r1), (y1+r1)+1):
            if (x1-i)**2 + (y1-j)**2 == r1**2:
                ryu.append((i,j))

    for k in range((x2-r2), (x2+r2)+1):
        for p in range((y2-r2), (y2+r2)+1):
            if (x2-k)**2 + (y2-p)**2 == r2**2:
                if (k, p) in ryu:
                    count_+=1

    
    print(count_)
