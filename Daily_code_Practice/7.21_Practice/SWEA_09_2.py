import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    N1 = N # 1N , 2N, 3N, 4N, 하는 방법
    num = set() #반복문 제거를 통해 0 ~ 9 숫자 1만 채울 수가 있음

    while True:
        for chr in str(N): # 안의 자리수를 보기 위해 문자열로 변환
            num.add(chr) # str로 쪼개진 숫자들이 set으로 인해 중복제거 되어 채워진다.
        if len(num) == 10:   #0~9의 길이는 10이기때문에
            break            # 10이 되었을때 멈춘다.
        N += N1   # 그게 아니라면 계속 1N, 2N, 3N, 4N 더해나간다.
    print(f'#{test_case} {N}')
 # 강사님 풀이 참고 하여 다시 풀어보았습니다.