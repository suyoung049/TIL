from collections import Counter
a, b, c, d = 	4, 1, 4, 4
# 카운터 함수 사용법
def solution(a, b, c, d):
    num_li = [a, b, c, d]
    # most_common은 카운터 함수에서 가장 많은 수로 리스트를 리턴
    # 그냥 counter는 객체 즉 딕셔너리 형태로 리턴
    count_li = Counter(num_li).most_common()
    sort_num = sorted(count_li, key=lambda x:x[1])
    # 4개 모두 동일한 경우
    if (len(count_li) == 1):
        answer = 1111 * count_li[0][0]
    # 2개 동일 나머지 2개 다른 경우
    elif (len(count_li) == 3):
         answer = count_li[1][0] * count_li[2][0]
    elif (len(count_li) == 2):
        # 3개 동일 1개 다른 경우
        if (count_li[0][1] != count_li[1][1]):
            print('111111111111')
            print(count_li[0][0])
            print(count_li[1][0])
            answer = (10 * count_li[0][0] + count_li[1][0]) ** 2
        else:
            answer = (count_li[0][0] + count_li[1][0]) * abs(count_li[0][0] - count_li[1][0])
    else:
        answer = min(num_li)
    print(answer)
    answer = 0
    return answer



solution(a, b, c, d)



