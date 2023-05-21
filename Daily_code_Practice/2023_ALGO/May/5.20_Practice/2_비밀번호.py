import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

door = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, "*", "*"]]

T = int(input())

for _ in range(T):
    result = 0
    num_ = int(input())

    i = 1
    dp = [[1] * 3 for _ in range(4)]
    while True:
        if num_ == i:
            for j in range(4):
                for i in range(3):
                    if door[j][i] != "*":
                        result += dp[j][i]
            
        else:
            for j in range(4):
                for i in range(3):
                    
                    nj = j + dy[i]
                    ni = i + dx[i]

                    if 0 <= nj < 4 and 0 <= ni < 3:
                        dp[j][i] += dp[nj][ni]
                        

          
            
    
    
            







