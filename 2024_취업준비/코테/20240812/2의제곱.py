arr = [1, 2, 3, 4, 5, 6]
def solution(arr):
    answer = []
    length = len(arr)
    n = 0

    
    while (2 ** n < length ):
        n += 1
    
    for i in range(2**n - length):
        arr.append(0)
    return arr

solution(arr)