import sys
sys.stdin = open('1_input.txt', 'r')



chr_number = list(input().strip())


n = len(chr_number)

num_li = []

for i in range(n):
    num_li.append(int(chr_number[i]))



def select_sort():
    for i in range(n-1):
        max = i

        for j in range(i+1, n):
            if num_li[j] > num_li[max]:
                max = j
        num_li[i], num_li[max] = num_li[max], num_li[i]

select_sort()

answer = ""
for i in range(len(num_li)):
    answer += str(num_li[i])

print(answer)