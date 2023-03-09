import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = list(input().split())
per_li = list(map(int, input().split()))

max_value = -10000000000000
min_value = 100000000000000

def dfs(depth, sum_ , hap, minu, gop, nanu):
    global max_value
    global min_value

    if depth == n:
        max_value = max(max_value, eval(sum_))
        min_value = min(min_value, eval(sum_))
        return
    
    if hap:
         dfs(depth + 1, sum_+'+'+ num_li[depth], hap-1, minu, gop, nanu)
    
    if minu:
        dfs(depth+1, sum_ + '-' + num_li[depth], hap, minu-1, gop, nanu)
    
    if gop:
        dfs(depth + 1, sum_ + '*' + num_li[depth], hap, minu, gop-1, nanu)
    
    if nanu:
        dfs(depth + 1, sum_ + '//' + num_li[depth], hap, minu, gop, nanu-1)


dfs(1, num_li[0], per_li[0], per_li[1], per_li[2], per_li[3])

print(max_value)
print(min_value)
