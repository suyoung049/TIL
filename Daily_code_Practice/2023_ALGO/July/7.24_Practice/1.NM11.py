import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

answer = []

def dfs(cnt, com_num):
    if cnt == m:
        answer.append(com_num)
        return
    
    prev_num = 0
    for i in range(n):
        if num_list[i] != prev_num:
            prev_num = num_list[i]
            dfs(cnt+1, com_num + [num_list[i]])

com_num = []
dfs(0,com_num)

for j in answer:
    print(*j)