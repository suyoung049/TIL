# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("4_나는요리사다.txt")
idx = 0                  # 몇 번째 참가자인지 번호 지정
bord = -1000              # 최대 점수를 bord로 변수 지정
for i in range(5):         # 참가자 5명 점수 넣기 위한 레인지 설정
    score = list(map(int, input().split()))   # 각 참가자 4개의 점수 
    if sum(score) > bord:         #만약 참가자의 총합이 최대값보다 크면 최대값이 
        bord = sum(score)         # 참가자의 총합으로 변경 되고
        idx = i+1                 # 순서도 1씩 증가한다 허나 그렇지 않으면 순서는 그대로 유지 
print(idx, bord)