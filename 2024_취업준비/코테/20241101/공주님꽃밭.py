import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


# 꽃의 피고 지는 날을 정렬하기 쉽게 숫자로 변경
def day_convert_num(month, day):
    day_num = 0
    month_li = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(month):
        day_num += month_li[i]
    
    day_num += day

    return day_num

n = int(input())

flower_li = []
for _ in range(n):
    st_m, st_d, end_m, end_d = map(int, input().split())
    start_num = day_convert_num(st_m, st_d)
    end_num = day_convert_num(end_m, end_d)
    flower_li.append((start_num, end_num))


sort_flower = sorted(flower_li, key=lambda x:(x[0], x[1]))
end_num = day_convert_num(11, 30)
target_end = day_convert_num(3, 1)
cnt = 0
max_end = 0

# 조건에 맞게 꽃을 심었을때 마지막 꽃의 지는날이 11월 30일 보다 커야함
while target_end <= end_num:
    candidate_li = []

    for flower in sort_flower:
        if flower[0] <= target_end:
            # 재차 반복시 전에 선택된 꽃 선택 방지
            if flower[1] <= max_end:
                continue
            candidate_li.append(flower[1])
        else:
            break
    
    if not candidate_li:
        cnt = 0
        break  # 무한 루프를 방지하기 위해 반복문 종료
    
    # 가장 멀리까지 피어 있는 꽃을 선택
    target_end = max(candidate_li)
    max_end = max(candidate_li)
    cnt += 1

print(cnt)
