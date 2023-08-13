import sys
sys.stdin =  open("1_input.txt", "r")
input = sys.stdin.readline


n = int(input())
arr = [list(input())+[0] for _ in range(n)]+[[0]*(n+1)]
arr_t = list(map(list, zip(*arr)))



def count(lst):
    cnt = ans = 1
    for i in range(1, len(lst)):
        if lst[i]==lst[i-1]:
            cnt+=1
            ans = max(ans, cnt)
        else:
            cnt=1
    return ans

def solve(arr):
    mx = 0
    for i in range(n-1):
        for j in range(0,n):
            # 오른쪽 사탕과 교환
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
            mx = max(mx, count(arr[i]))
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]

            # 아래쪽 사탕과 교환
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
            mx = max(mx, count(arr[i]),count(arr[i+1]))
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
    return mx

ans = max(solve(arr), solve(arr_t))
print(ans)