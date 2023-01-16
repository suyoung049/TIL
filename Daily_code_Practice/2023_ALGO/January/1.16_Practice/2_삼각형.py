import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

while True:
    tri = list(map(int, input().split()))
    if tri == [0, 0, 0]:
        break
    else:
        tri.sort()
        
        if (tri[0])*(tri[0]) + (tri[1])*(tri[1]) == (tri[2])*(tri[2]):
            print('right')

        else:
            print('wrong')