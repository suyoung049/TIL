# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a, b = map(str, input().split())
Rev_a = int(a[::-1])
Rev_b = int(b[::-1])
if Rev_a > Rev_b:
    print(Rev_a)

else:
    print(Rev_b)