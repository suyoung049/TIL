import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
money_li = list(map(int, input().split()))
budget = int(input())

result = 0
start = 0
end = max(money_li)


while True:
    sum_ = 0
    if start > end:
        break

    mid = (start + end)//2

    for money in money_li:
        if money > mid:
            sum_ += mid
        
        else:
            sum_ += money

    
    if sum_ > budget:
        end = mid -1

    else:
        start = mid + 1
        result = mid

print(result)

