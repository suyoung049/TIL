import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(map(int, input().split()))

result = answer = sum(num_li[:k])


for i in range(k, n):
    answer = answer + num_li[i] - num_li[i-k]
    result = max(result, answer)
    
print(result)