import sys

sys.stdin = open("자료구조최고_input.txt", "r") 

N, M = map(int, input().split())
book_1 = int(input())
book_list_1 = list(map(int, input().split()))
book_2 = int(input())
book_list_2 = list(map(int, input().split()))
stack = []
while len(book_list_1) and len(book_list_2) != 0:
    stack.append(book_list_1.pop())
    stack.append(book_list_2.pop())
if len(book_list_1) > len(book_list_2):
    stack.append(book_list_1[0])
elif len(book_list_1) < len(book_list_2):
    stack.append(book_list_2[0])
else:
    stack
if stack == sorted(stack):
    print('YES')
else:
    print('NO')

# 이 경우 무조건 첫번째 두번째 더미 순으로만 정렬되므로 틀린 코드이다.
