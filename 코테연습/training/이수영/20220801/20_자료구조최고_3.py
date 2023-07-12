import sys

sys.stdin = open("자료구조최고_input.txt", "r") 
input = sys.stdin.readline

N, M = map(int, input().split())
answer = 'Yes'
for _ in range(M):
    n = int(input())
    list_ = list(map(int, input().split()))
    comparison = list_.pop()
    while len(list_) != 0:
        if list_[-1] > comparison:
            comparison = list_.pop()
        else:
            answer = 'No'
            break
    if answer == 'No':
        break
print(answer)

      