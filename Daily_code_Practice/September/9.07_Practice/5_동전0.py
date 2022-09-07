import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

money = sorted(money, reverse=True)
count = 0

if m >= money[0]:
    a = m//money[0]
    count = a
    m = m % money[0]
    

for i in range(1,n):
    if money[i] <= m < money[i-1]:
        a = m//money[i]
        count += a
        m = m % money[i]
        if m == 0:
            break
print(count)

