import sys
input = sys.stdin.readline


n = int(input())

for _ in range(n):
    stone = int(input())

    start = 0
    end = 10 ** 9

    while start <= end:
        mid = (start + end) //2
        # 공차가 1인 공차수열의 합 (n+1)n /2
        stone_sum = ((mid +1) * mid)//2

        if stone_sum <= stone:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(answer)