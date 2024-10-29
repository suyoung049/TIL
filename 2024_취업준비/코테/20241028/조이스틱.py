name  = "AAB"
from copy import deepcopy

stick = 0
min_left = 100
def solution(name):
    global stick
    global min_left
    answer = 0
    name_li = list(name)
    length = len(name_li)
    check_idx = []
    for idx in range(length):
        if name_li[idx] != "A":
            stick += change_alpha(name_li[idx])
            if idx != 0:
                check_idx.append(idx)
    left_right = 0
    dfs(check_idx, left_right, length, 0)

    answer = stick + min_left

    return answer

def dfs(change_idx, left_right, length, start):
    global min_left
    if not change_idx:
        min_left = min(min_left, left_right)
        return
    
    dx = [0, -1]
    
    for x in range(2):
        # 각 반복에서 `copy_idx`를 새롭게 복사합니다.
        copy_idx = deepcopy(change_idx)
        
        if dx[x] == 0:
            idx = copy_idx.pop(0)
            if idx > start:
                right = idx - start
            else:
                right = idx + (length - start)
            dfs(copy_idx, left_right + right, length, idx)
        else:
            idx = copy_idx.pop()
            if idx > start:
                left = start + (length - idx)
            else:
                left = start - idx
            dfs(copy_idx, left_right + left, length, idx)
            

def change_alpha(alpha):
    cnt = 0
    asc_num = ord(alpha)
    if asc_num > 78:
        cnt = 90 - asc_num + 1
    else:
        cnt = asc_num - 65

    return cnt


print(solution(name))