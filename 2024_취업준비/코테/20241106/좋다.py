import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pointer(num_list, target, exclude_index):
    left = 0
    right = len(num_list) - 1

    # target + 0 = target 예외처리 
    while left < right:
        if left == exclude_index:
            left += 1
            continue
        if right == exclude_index:
            right -= 1
            continue
            
        num_sum = num_list[left] + num_list[right]
        
        if num_sum == target:
            return True
        elif num_sum > target:
            right -= 1
        else:
            left += 1

    return False

n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
good = 0

for i in range(n):
    target = num_list[i]
    if pointer(num_list, target, i):  # i번째 수를 제외하고 검사
        good += 1

print(good)
    


