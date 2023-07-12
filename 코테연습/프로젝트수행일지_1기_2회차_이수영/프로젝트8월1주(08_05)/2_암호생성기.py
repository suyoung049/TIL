import sys

sys.stdin = open("_암호생성기.txt")

while True:
        try:
                test_case = int(input())
                data = list(map(int, input().split()))
                cnt = 1
                while True:
                        value = data.pop(0)
                        value -= cnt
                        if value <= 0 :
                                data.append(0)
                                break
                        data.append(value)
                        if cnt >= 5:
                                cnt = 0
                        cnt += 1
                print(f'#{test_case}', *data)
        except:
                break

