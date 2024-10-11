user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
from copy import deepcopy
answer_li = []
rs = []

def solution(user_id, banned_id):
    global answer_li
    # 하나의 제제아이디가 user_id들에 매핑 되는지 확인하는 딕셔너리
    convert_li = []

    for bid in banned_id:
        convert_li.append([is_convert(uid, bid) for uid in user_id])
    print(convert_li)
    
    dfs(user_id, banned_id, convert_li, 0, check_li=[False for _ in range(len(user_id))])
    
    return len(answer_li)


# 제제아이디가 각각의 유저 아이디에 매핑이 되는지 확인
def is_convert(uid, bid):
    if len(uid) != len(bid):
        return False
    
    for i, ch in enumerate(uid):
        if bid[i] == "*":
            continue
        elif ch != bid[i]:
            return False
        
    return True

def dfs(user_id, banned_id, convert_li, b_idx, check_li):
    global answer_li, rs
    # 재재 아이디가 모두 매칭 되었을 경우
    if b_idx == len(banned_id):
        temp = deepcopy(rs)
        temp.sort()
        if not answer_li.__contains__(temp):
            answer_li.append(temp)
        return
    
    for idx, ch in enumerate(user_id):
        if check_li[idx]:
            continue
        if not convert_li[b_idx][idx]:
            continue
        check_li[idx] = True
        rs.append(ch)
        dfs(user_id, banned_id, convert_li, b_idx + 1, check_li)
        check_li[idx] = False
        rs.pop()

print(solution(user_id, banned_id))