arry = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arry)):
    min_idx = i
    for j in range(i+1, len(arry)):
        if arry[min_idx] > arry[j]:
            min_idx = j
    
    arry[i], arry[min_idx] = arry[min_idx], arry[i]

print(arry)

for i in range(1, len(arry)):
    for j in range(i, 0, -1):
        if arry[j] < arry[j -1]:
            arry[j], arry[j-1] = arry[j-1], arry[j]
        else:
            break
print(arry)

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(arry, 0, len(arry)-1)
print(arry)


count = [0] * (max(arry) + 1)

for i in range(len(arry)):
    count[arry[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')