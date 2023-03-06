import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

print(num_li)