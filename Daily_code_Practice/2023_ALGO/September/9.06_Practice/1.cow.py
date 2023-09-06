import sys
sys.stdin = open('1_input.txt', "r")
input = sys.stdin.readline

n, q = map(int, input().split())

cow_li = [0]

for _ in range(n):
    cow_num = int(input())
    cow_li.append(cow_num)

a_cow = [0] * (n+1)
b_cow = [0] * (n+1)
c_cow = [0] * (n+1)

for j in range(1, n+1):
    if cow_li[j] == 1:
        a_cow[j] += 1
    elif cow_li[j] == 2:
        b_cow[j] += 1
    else:
        c_cow[j] += 1

    a_cow[j] += a_cow[j-1]
    b_cow[j] += b_cow[j-1]
    c_cow[j] += c_cow[j-1]

answer = []

for _ in range(q):
    start, end = map(int, input().split())
    a_answer = a_cow[end] - a_cow[start-1]
    b_answer = b_cow[end] - b_cow[start-1]
    c_answer = c_cow[end] - c_cow[start-1]
    answer.append((a_answer, b_answer, c_answer))

for lst in answer:
    print(*lst)
    