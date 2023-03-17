import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

num_li = []

while True:
    try:
        num_ = int(input())
        num_li.append(num_)

    except:
        break

def dfs(start, end):
    if start > end:
        return
    
    # 큰 수가 없을 경우
    mid = end + 1

    for i in range(start+1, end+1):
        if num_li[start] < num_li[i]:
            mid = i
            break
    
    dfs(start+1, mid-1)
    dfs(mid, end)
    print(num_li[start])


dfs(0, len(num_li) -1)

