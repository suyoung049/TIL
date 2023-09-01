stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
answer = 0
start = 1
end = max(stones)

while start <= end:
    mid = (start + end)//2
    lst = []
    cnt = 1
    for i in range(len(stones)):
        if mid >= stones[i]:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 1
    # 마지막 건너 뛰기 
    lst.append(cnt)
    if max(lst) > k:
        end = mid -1
    else:
        start = mid + 1
        answer = start

print(answer)

  

    
