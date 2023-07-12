# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())
c = int(input())
multiple = (a * b * c)
num = [0] * 10
digits = str(multiple)
for idx in range(len(digits)):
    num[int(digits[idx])] += 1
print(num)
j = 0
for j in range(len(num)):
    print(num[j])
    j += 1

a=int(input())
b=int(input())
c=int(input())
n=list(str(a*b*c))
for i in range(10):      # 0 ~9 까지의 수가 만들어진다
    print(n.count(str(i)))    # count 함수로 갯수를 샌다.