# 기본 적인 버블 정렬
def bubbleSort(arr):
  length = len(arr) -1

  for i in range(length):
    for j in range(length-i):
      if (arr[j] > arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]

  
  return arr


# 개선된 버블 정렬(최선의 경우 시간복잡도를 O(N)으로 낮출수 있음)
def bubble_modified(arr):
  length = len(arr) -1

  for i in range(length):
    isSort = False

    for j in range(length- i):
      if (arr[j] > arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]

        isSort = True

    if isSort == False:
      break
  
  return arr

# 삽입 정렬
def insertSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1

    arr[j+1] = arr[j]
    j -= 1

    arr[j+1] = key


# 선택 정렬
def selectSort(arr):
  for i in range(len(arr)-1):
    min_index = 1

    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [4, 8, 5]

# 병합 정렬
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
   

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
      if left[i] < right[i]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1
    
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  return arr

mergeSort(arr)
print(arr)
