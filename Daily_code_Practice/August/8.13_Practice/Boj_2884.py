import sys

sys.stdin = open("2884_input.txt", "r")

N, M = map(int, input().split())

if M > 44:
    print(N , M-45)
elif M <= 44 and N >=1:
    print(N-1,M+15)
else:
    print(23, M+15)
