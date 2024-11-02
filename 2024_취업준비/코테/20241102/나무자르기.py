import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
tree_li = list(map(int, input().split()))

start = 1
end = 2000000000
answer = 0

while start <= end:
    tree_sum = 0
    mid = (start + end)//2

    for tree in tree_li:
        if mid >= tree:
            continue
        else:
            tree_sum += (tree - mid)
    
    if m > tree_sum:
        end = mid -1
    
    else:
        answer = mid
        start = mid + 1

print(answer)