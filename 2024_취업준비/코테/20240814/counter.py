from collections import Counter
array, n = [1, 1, 2, 3, 4, 5], 1
def solution(array, n):
   
    array_counter = Counter(array)
    print(array_counter)
    
    return array_counter[n]
solution(array, n)

