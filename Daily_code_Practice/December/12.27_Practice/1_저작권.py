import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

print((a*(b-1)+1))
