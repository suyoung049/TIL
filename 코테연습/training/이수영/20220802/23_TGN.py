import sys

sys.stdin = open("23_input.txt", "r")
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    adv = list(map(int, input().split()))
    if (adv[1] - adv[2]) > adv[0]:
        print('advertise')
    elif (adv[1] - adv[2]) == adv[0]:
        print('does not matter') 
    else:
        print('do not advertise')