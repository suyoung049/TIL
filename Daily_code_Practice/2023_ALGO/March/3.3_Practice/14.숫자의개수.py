import sys
sys.stdin = open('14_input.txt', 'r')
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

gop = a * b * c

for i in range(10):
    gop = str(gop)
    i = str(i)
    count_ = gop.count(i)
    print(count_)