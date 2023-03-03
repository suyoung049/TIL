import sys
sys.stdin = open('20_input.txt', 'r')
input = sys.stdin.readline

a, b, v = map(int, input().split())

if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else: # 달팽이가 올라간 높이가 모자랄때 
    print((v-b)//(a-b) + 1)