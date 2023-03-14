import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

m, n, l = map(int, input().split())

shout_list = list(map(int, input().split()))

shout_list.sort()

animal_place = []
for _ in range(n):
    y, x = map(int, input().split())
    animal_place.append((y,x))

animal_place = sorted(animal_place, key=lambda x:(x[0], x[1]))

# 그냥 이분 탐색 문제???????

count_ = 0
idx = 0
for y, x in animal_place:
    start = 1
    end = len(shout_list) - 1

    while True:
        if start > end:
            break
        
        mid = (start + end)//2

        if shout_list[mid] < y:
            start = mid + 1
            idx = mid

        else:
            end = mid -1
      
    if abs(shout_list[idx] - y) + x <= l:
        count_ += 1
    
    elif idx + 1 < len(shout_list) and abs(shout_list[idx + 1] -y) + x <= l:
        count_ += 1

    elif idx > 0 and abs(shout_list[idx-1] - y) + x <= l:
        count_ += 1 

print(count_)




