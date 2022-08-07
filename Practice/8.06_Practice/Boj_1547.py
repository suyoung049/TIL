import sys

sys.stdin = open("1547_input.txt", "r")
N = int(input())
cup = [1, 2, 3]
for _ in range(N):
    x , y = map(int, input().split())
    xi = cup.index(x)
    yi = cup.index(y)
    cup[xi], cup[yi] = cup[yi], cup[xi]
print(cup[0])