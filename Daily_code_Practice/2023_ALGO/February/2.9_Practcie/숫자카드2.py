import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
check = list(map(int, input().split()))

check_li = {}

for i in card:
    if i in check_li:
        check_li[i] += 1
    else:
        check_li[i] = 1

def bi(ch, j):
    start = 0
    end = len(ch) - 1

    while True:
        if start > end:
            break

        mid = (start+end)//2

        if j == ch[mid]:
            return check_li[j]

        elif j > ch[mid]:
            start = mid + 1
        else:
            end = mid-1
    return 0


for j in check:
    print(bi(card, j), end =' ')