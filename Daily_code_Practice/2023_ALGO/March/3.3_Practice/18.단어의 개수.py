import sys
sys.stdin = open('18_input.txt', 'r')
input = sys.stdin.readline

text = input().split()
print(len(text))