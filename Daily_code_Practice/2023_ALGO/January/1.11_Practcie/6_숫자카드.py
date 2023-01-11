import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))
num_li.sort()
m  = int(input())
surch = list(map(int, input().split()))

check = dict()

for i in num_li:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

def s(num_li, x):
    start = 0
    end = len(num_li) - 1

    while True:
        if start > end:
            break
        else:
            mid = (start + end) // 2

            if x == num_li[mid]:
                return check[x]

            elif x > num_li[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
    
    return 0

for i in range(m):
    print(s(num_li, surch[i]), end=' ')