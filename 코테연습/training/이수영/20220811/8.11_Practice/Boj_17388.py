import sys

sys.stdin = open("17388_input.txt", "r")

S, K, H = list(map(int, input().split()))

if (S + K + H) >= 100:
    print('OK') 
else:
    if S < K and S < H:
        print('Soongsil') 
    elif K < S and K < H:
        print('Korea')
    elif H < S and H < K:
        print('Hanyang')