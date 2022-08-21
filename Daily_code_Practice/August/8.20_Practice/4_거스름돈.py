import sys
sys.stdin = open('4_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    money_list = [0] *8
    money = int(input())
    while money >= 50000:
        money -= 50000
        money_list[0] += 1
    while money >= 10000:
        money -= 10000
        money_list[1] += 1
    while money >= 5000:
        money -= 5000
        money_list[2] += 1
    while money >= 1000:
        money -= 1000
        money_list[3] += 1
    while money >= 500:
        money -= 500
        money_list[4] += 1
    while money >= 100:
        money -= 100
        money_list[5] += 1
    while money >= 50:
        money -= 50
        money_list[6] += 1
    while money >= 10:
        money -= 10
        money_list[7] += 1
    print(f'#{test_case}')
    print(*money_list)

    