import sys
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

money = int(input())

answer = 1000 - money

money_li = [500, 100, 50, 10, 5, 1]


result = 0
for i in range(len(money_li)):
    if answer >= money_li[i]:
        result += answer//money_li[i]
        answer = answer % money_li[i]

    if answer == 0:
        break

print(result)