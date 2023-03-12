import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
tree_li = list(map(int, input().split()))



start = 0
end = max(tree_li)

result = 0

while True:
    if start > end:
        break

    total = 0
    mid = (start + end)//2



    for tree in tree_li:
        if tree > mid:
            total += (tree-mid)

    if total < m:
        end = mid -1
    
    else:
        result = mid
        start = mid + 1

print(result)
    
