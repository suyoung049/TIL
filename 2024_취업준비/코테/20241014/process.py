priorities, location = [1, 1, 9, 1, 1, 1], 0
def solution(priorities, location):
    length = len(priorities)
    que = []
    cnt = 0
    for i in range(length):
        que.append((priorities[i], i))

    # 큰 숫자 부터 정렬해서 풀기(핵심)
    priorities.sort(reverse= True)

    while que:
        process = que.pop(0)
        if process[0] == priorities[0]:
            cnt += 1
            priorities.pop(0)
            if location == process[1]:
                return cnt
        else:
            que.append(process)
       
print(solution(priorities, location))