import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
re_N = n
count = 0

while True:
    a = re_N // 10 # 주어진 수의 앞자리수
    b = re_N % 10  # 주어진 수의 뒷자리수 
    c = (a + b) % 10
    re_N = (b * 10 + c)
    count += 1
    if re_N == n:
        break

print(count)

    

