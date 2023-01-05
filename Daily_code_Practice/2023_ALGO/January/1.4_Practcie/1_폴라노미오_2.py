import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

bord = input()

bord = bord.replace("XXXX", "AAAA")
bord = bord.replace("XX", "BB")

if "X" in bord:
    print(-1)

else:
    print(bord)