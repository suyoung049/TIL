import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(map(int, input().split()))

answer = num_li.count(k)


for j in range(2, n):
    if sum(num_li) == k:
        answer = 1
        break
    
    else:
        sum_result = sum(num_li[:j])
        if sum_result == k:
            answer += 1
        
        for i in range(j, n):
            sum_result = sum_result + num_li[i] - num_li[i-j]
            if sum_result == k:
                answer += 1

print(answer)