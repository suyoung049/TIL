import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))
per_li = list(map(int, input().split()))


min_value = 100000000000000000000
max_value = -10000000000000000000000

def dfs(depth, sum_, hap, minu, gop, nanu):
    global min_value
    global max_value

    if depth == n:
        min_value = min(min_value, sum_)
        max_value = max(max_value, sum_)
        return
    

    if gop:
        dfs(depth+1, sum_ * num_li[depth], hap, minu, gop-1, nanu)
    if nanu:
        dfs(depth+1, int((sum_ / num_li[depth])), hap, minu, gop, nanu-1)
    if hap:
        dfs(depth+1, sum_ + num_li[depth], hap-1, minu, gop, nanu)
    if minu:
        dfs(depth+1, sum_ - num_li[depth], hap, minu-1, gop, nanu)
    
    


dfs(1, num_li[0], per_li[0], per_li[1], per_li[2], per_li[3])

print(max_value)
print(min_value)