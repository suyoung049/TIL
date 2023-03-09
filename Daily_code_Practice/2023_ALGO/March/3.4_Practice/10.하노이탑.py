import sys
sys.stdin = open('10_input.txt', 'r')
input = sys.stdin.readline

def hanoi_f(start, end, middle,  n):
    if n == 1:
        print(start,end)
        return

    hanoi_f(start, middle, end, n-1) #1단계 (1->2)
    hanoi_f(start, end, middle,  1) #2단계 (마지막원반 1->3)
    hanoi_f(middle, end, start, n-1) #3단계 (2->3)

#메인
n = int(input())
print(2**n-1)
if n <= 20:
    hanoi_f(1,3,2,n)