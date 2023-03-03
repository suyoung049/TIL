import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    a, b = map(int, input().split())
    print(a + b)