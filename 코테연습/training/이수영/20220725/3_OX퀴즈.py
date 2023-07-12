# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(T):
    quiz = input()
    result = 0
    cnt = 0          
    for j in quiz:
        if j == 'O':       # 입력된 문자열에 O가 있다면 숫자를 1씩 계속 더한다
            cnt += 1
            result += cnt
        else:
            cnt = 0         # 그게 아니라면 cnt를 0으로 리셋
    print(result)

n=int(input())
cnt=int(0)
result=int(0)
for i in range(n):
    a=input()
    for j in range(len(a)):   # 주어진에 문자열이 아닌경우 리스트로 인덱스화 한다.
        if a[j] == 'O':
            cnt += 1
            result += cnt
        elif a[j] == 'X':
            cnt=0
    print(result)
 