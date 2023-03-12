import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_li = list(map(int, input().split()))
num_li.sort()
m = int(input())
target_li = list(map(int, input().split()))


def binary_search(array, target):
    start = 0
    end = n-1

    while True:
        if start > end:
            break

        mid = (start+end)//2

        if array[mid] == target:
            return 1

        elif array[mid] > target:
            end = mid -1
        
        else:
            start = mid + 1
    
    return 0

for target in target_li:
    print(binary_search(num_li, target))
