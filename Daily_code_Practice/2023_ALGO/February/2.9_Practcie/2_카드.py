import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
check = list(map(int, input().split()))

def bi(ca, i):
    start = 0
    end = len(ca)-1

    while True:
        if start > end:
            break
        mid = (start+end)//2

        if i == ca[mid]:
            return 1
        
        elif i > ca[mid]:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return 0


for i in check:
    print(bi(card, i), end = ' ')