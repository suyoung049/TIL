
arr = [1,1,3,3,0,1,1]
answer = []


for i in range(len(arr)):

    if arr[i] not in answer:
        answer.append(arr[i])
    
    else:
        if answer[-1] != arr[i]:
            answer.append(arr[i])