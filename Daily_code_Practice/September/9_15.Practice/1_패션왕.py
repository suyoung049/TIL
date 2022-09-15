import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    dict_ = {}
    count = 1
    n = int(input())
    for _ in range(n):
        v, k = input().split()

        if k in dict_:
            dict_[k] += 1

        else:
            dict_[k] = 1

    for k in dict_:
        count *= (dict_[k] +1)    # 안입는 경우 까지 더해줘서 + 1

    print(count-1)                # 전부 안입는 경우는 제외
    
       


