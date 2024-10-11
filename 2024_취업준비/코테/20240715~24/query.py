arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

def solution(arr, queries):
    answer = []
    for query in queries:
       
        
        min = 999999999999999999999999999999
        for i in range(query[0], query[1]+1):
            if arr[i] > query[2]:
             
              if min > arr[i] :
                  min = arr[i]
                 
        if min == 999999999999999999999999999999:
            min = -1
        answer.append(min)
           
            
    
    return answer

solution(arr, queries)

