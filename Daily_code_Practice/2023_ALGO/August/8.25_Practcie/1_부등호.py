import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())
sign_li = list(input().split())
max_num, min_num = "", ""
check = [0] * 10


def possible(j, i, sign):
    if sign == "<":
        if j < i :
            return True
        else:
            return False
    else:
        if j > i:
            return True
        else:
            return False
    

def dfs(cnt, tlist):
    global max_num, min_num
    if cnt == n + 1:
        if len(min_num) == 0:
            min_num = tlist
        else:
            max_num = tlist
        
        return
    
    for i in range(10):
        if check[i] == 0:
            if cnt == 0 or possible(int(tlist[-1]), i, sign_li[cnt-1]):
                check[i] = -1
                dfs(cnt +1, tlist + str(i))
                check[i] = 0

dfs(0, "")
print(max_num)
print(min_num)