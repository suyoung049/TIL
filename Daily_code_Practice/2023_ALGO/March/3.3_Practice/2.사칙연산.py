import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline
A, B = map(int, input().split())


print(A + B)
print(A - B)
print(A * B)
print(A//B)
print(A%B)