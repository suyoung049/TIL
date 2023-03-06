import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))
opearter = list(map(int, input().split()))

max_va = -1000000000000
min_va = 10000000000000000000000000


def dfs(deph, num_, hap, minu, gop, na):
    global max_va
    global min_va

    if deph == n:
        max_va = max(num_, max_va)
        min_va = min(num_, min_va)
        return

    if hap:
        dfs(deph+1, num_ + num_li[deph], hap-1, minu, gop, na)
    if minu:
        dfs(deph+1, num_ - num_li[deph], hap, minu-1, gop, na)
    if gop:
        dfs(deph+1, num_ * num_li[deph], hap, minu, gop-1, na)
    if na:
        dfs(deph+1, int((num_/num_li[deph])), hap, minu, gop, na-1)
    
dfs(1, num_li[0], opearter[0], opearter[1], opearter[2], opearter[3])

print(max_va)
print(min_va)