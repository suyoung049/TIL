import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
k = int(input())


start = 1
end = n*n

idx = 0
while True:
    if start > end:
        break

    mid = (start + end)//2

    count_ = 0
    for i in range(1, n+1):
        count_ += min(mid//i , n)
    

    if count_ < k:
        start = mid + 1
    
    
    else:
        end = mid-1

print(start)