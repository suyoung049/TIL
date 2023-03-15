import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())


def moo(acc, cur, N):
    # Moo(n-1)의 길이는 Moo(n)의 길이에서 가운데 부분의 길이를 뺀 후 2로 나눈 것과 같다.
    prev = (acc-cur)//2
    # 왼쪽 Moo(n-1)부분에 N이 존재하면 사실상 Moo(n-1)의 N번째 문자를 찾는 것과 같다.
    if N <= prev:
        return moo(prev, cur-1, N)
    # 오른쪽 Moo(n-1) 부분에 N이 존재하면 Moo(n-1)의 (N - Moo(n-1)의 길이 - 가운데 부분 길이)번째 문자를 찾는 것과 같다.
    elif N > prev + cur:
        return moo(prev, cur-1, N-prev-cur)
    # 가운데 부분에 N이 존재한다면 바로 N번째 문자를 알 수 있다.
    else:
        if N - prev -1:
            return 'O'
        # 즉 N이 가운데 부분의 첫번째라면 m이고 그렇지 않다면 o 이다.
        else:
            return 'm'



# 먼저 길이가 N번째 문자를 찾으려면 Moo(n)의 길이가 N이상이어야 하므로, while 문에서 이를 만족하는 n을 찾는다.
acc, k = 3, 0
while True:
    if n <= acc:
        break
    
    k += 1
    acc = acc *2 + k + 3

# moo 함수에는 Moo(n)의 길이, 가운데 부분의 길이, N이 매개 변수로 주어진다.
print(moo(acc, k+3, n))

