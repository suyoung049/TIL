# https://www.acmicpc.net/problem/2846
import sys

sys.stdin = open("6_오르막길.txt")
n = int(input())                
up_hill = list(map(int, input().split()))
a = 0               # a 값 초기화
lenth = []            # max 값 사용 위해 리스트 설정
for i in range(n-1):     # 정수가 5개 주어지면 인덱스는 n-1인 4까지
    if up_hill[i] < up_hill[i+1]:   # 오르막길
        a += up_hill[i+1] - up_hill[i]   # 차이 a의 총합이 높이
    else:                    # 아닌경우는 평지, 내리막길
        lenth.append(a)        # 지금까지의 오르막길 높이 리스트에 입력
        a = 0                  # 다시 0 으로 초기화
lenth.append(a)              # 여러번 반복후 모든 반복이 끝나면 높이들 리스트 입력
print(max(lenth))            # 최대 높이 출력