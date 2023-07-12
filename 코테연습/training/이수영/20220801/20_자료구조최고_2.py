import sys

sys.stdin = open("자료구조최고_input.txt", "r") 
input = sys.stdin.readline

N, M = map(int, input().split())
chk = True
for _ in range(M):
    n = int(input())
    list_ = list(map(int, input().split()))
    if chk:
        while len(list_) > 0:
            book_num = list_.pop()
            
            if list_:
                if book_num > list_[-1]:
                    chk = False
                    break
    else:
        break
if chk:
    print('Yes')
else:
    print('No')
