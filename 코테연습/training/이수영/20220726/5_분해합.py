# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("5_분해합.txt")


N = int(input())   # 216을 입력받아 정수로 변환
decom = 0          # 분해합을 0으로 초기화
for i in range(1, N+1): #  1부터 216까지 정수 범위의 레인지 생성
    seq = list(map(int, str(i)))   # i = 124 lit[1, 2, 4]
    decom = i + sum(seq)           # sum 함수 사용을 위해 다시 정수로 map활용
    if decom == N:
        print(i)
        break
else:                     # 값이 같을때 멈추면 최소값
                          # if-else 가 아니라 for - else로 사용
    
    print('0')                  # 없을 시 0