import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    h, w, n = map(int, input().split())
    
    con = 0
    first = 0

    if n%h == 0:                # 손님의 차례가 층을 나누었을때 나머지가 0이면
        con = h * 100           # 호텔의 마지막 층 즉 h * 100이다
        first = n//h            # 호수는 차례 나누기 층의 몫이다

    else:
        con = (n%h) *100
        first = 1 + n //h        # 전부 위의 과정과 동일하나 차례 나누기 층의 나머지가
    print(con + first)           # 0이 아니라면 다음 호수로 넘어갔기 때문에
                                 # 호수는 1을 추가적으로 더해준다.