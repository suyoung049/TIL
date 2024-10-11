arr, query = [0, 1, 2, 3, 4, 5], [4, 1, 2]

def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if (i % 2 == 0):
            arr = arr[:query[i]+1]
            print(arr)
        else:
            arr = arr[query[i]:]
            print(arr)
    return answer

solution(arr, query)