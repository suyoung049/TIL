import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(map(int, input().split()))
answer = 0
check = True


for j in range(1, n):
    if check == False:
        break
    if j == 1:
        for card in num_li:
            if card >= k:
                answer = 1
                check = False
                break
    
    else:
        sum_num = sum(num_li[:j])
        if sum_num >= k:
            answer = j
            check = False
            break
        else:
            for i in range(j, n):
                sum_num = sum_num + num_li[i] - num_li[i-j]
                if sum_num >= k:
                    answer = j
                    check= False
                    break

print(answer)
