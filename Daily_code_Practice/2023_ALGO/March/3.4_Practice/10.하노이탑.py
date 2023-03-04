import sys
sys.stdin = open('10_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
start = 1
middle = 2
end = 3

rute = []

def hanoi(n, start, end, middle):
    

    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, middle, end)
    print(start, end)
    hanoi(n-1, middle, end, middle)


hanoi(n, start, end, middle)

print(len(rute))
for i in rute:
    print(i[0], i[1])