import sys

sys.stdin = open("42_input.txt", "r")
N,M = map(int, input().split())

park_land = [list(input()) for _ in range(N)]


car = [0] * 5


for i in range(N-1):
    for j in range(M-1):

        a = park_land[i][j]
        b = park_land[i+1][j]
        c = park_land[i][j+1]
        d = park_land[i+1][j+1]

        land = a + b + c + d

        for x in range(5):
            if land.count('X') == x and '#' not in land:
                car[x] += 1
for y in car:
    print(y)


        

                

                    

            