import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())   


num_li = []

for _ in range(n):
    num_li.append(int(input()))

# 그냥 버블 정렬
# def bubble_sort():
#     for i in range(n-1):
#         exchange = 0
#         for j in range(n-1, i, -1):
#             if num_li[j-1] > num_li[j]:
#                 num_li[j-1], num_li[j] = num_li[j], num_li[j-1]

# bubble_sort()


# 정렬이 멈주면 함수 중단 
# def bubble_sort():
#     for i in range(n-1):
#         exchange = 0
#         for j in range(n-1, i, -1):
#             if num_li[j-1] > num_li[j]:
#                 num_li[j-1], num_li[j] = num_li[j], num_li[j-1]
#                 exchange += 1
#         if exchange == 0:
#             break

# bubble_sort()

# 정렬 완료된 부분 스캔 범위 제한
# def bubble_sort():
#     k = 0
#     while k < n-1:
#         last = n-1
#         for i in range(n-1):
#             for j in range(n-1, k, -1):
#                 if num_li[j-1] > num_li[j]:
#                     num_li[j-1], num_li[j] = num_li[j], num_li[j-1]
#                     last = j
#         k = last

# bubble_sort()

# 그냥 셰이커 정렬
def bubble_sort():
    left = 0
    right = n - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if num_li[j-1] > num_li[j]:
                    num_li[j-1], num_li[j] = num_li[j], num_li[j-1]
                    last = j
        left = last

        for j in range(left, right):
            if num_li[j] > num_li[j+1]:
                num_li[j], num_li[j+1] = num_li[j+1], num_li[j]
                last = j
        
        right = last

bubble_sort()


for i in num_li:
    print(i)