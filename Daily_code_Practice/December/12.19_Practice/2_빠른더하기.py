import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)