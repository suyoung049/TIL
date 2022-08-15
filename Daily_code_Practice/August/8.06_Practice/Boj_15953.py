import sys

sys.stdin = open("15953_input.txt", "r")
T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())
    money = []
    if a == 1:
        money.append(int(5000000))
    elif 1 < a < 4:
        money.append(int(3000000))
    elif 3 < a < 7:
        money.append(int(2000000))
    elif 6 < a < 11:
        money.append(int(500000))
    elif 10 < a < 16:
        money.append(int(300000))
    elif 15 < a < 22:
        money.append(int(100000))
    else:
        money.append(int(0))
    
    if b == 1:
        money.append(int(5120000))
    elif 1 < b < 4:
        money.append(int(2560000))
    elif 3 < b < 8:
        money.append(int(1280000))
    elif 7 < b < 16:
        money.append(int(640000))
    elif 15 < b < 32: 
        money.append(int(320000))
    else:
        money.append(int(0))
    print(sum(money))