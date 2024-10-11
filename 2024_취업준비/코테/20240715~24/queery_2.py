arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

def solution(arr, queries):
    answer = []
    for query in queries:
    
        for i in range(query[0], query[1]+1):
            if (i % query[2] == 0):
                arr[i] += 1
    
    print(arr)
    return arr

solution(arr, queries)
           