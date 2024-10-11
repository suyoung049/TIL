stones = [1,2,3,4] 
k = 1
class group:
    def __init__(self, left, right):
        self.left = left
        self.right = right 

def solution(stones, k):
    answer = 0
    stones = [(num, idx) for idx, num in enumerate(stones)]
    sort_stones = sorted(stones, key=lambda x:x[0])

    check = [None for _ in range(len(stones))]
    index = 0
    max_len = 0
    min_nums = 0

    while index < len(stones):
        if max_len >= k:
            break
        answer += (sort_stones[index][0] - min_nums)
        min_nums = sort_stones[index][0]

        while sort_stones[index][0] == min_nums:
            stone = sort_stones[index]
            # 왼쪽의 그룹을 체크
            if stone[1] > 0 and check[stone[1] - 1]:
                left_group = check[stone[1] - 1]
                #왼쪽 그룹과 오른쪽 그룹에 모두 포함되어야 할때 합치는 과정
                if stone[1] + 1 < len(stones) and check[stone[1] + 1]:
                    right_group = check[stone[1] + 1]
                    left_group.right = right_group.right
                    l,r = right_group.left, right_group.right
                    for i in range(l, r+1):
                        check[i] = left_group
                else:
                    left_group.right = stone[1]
                check[stone[1]] = left_group
                max_len = max(max_len, left_group.right - left_group.left + 1)
            # 오른쪽 그룹을 체크
            elif stone[1] + 1 < len(stones) and check[stone[1] + 1]:
                right_group = check[stone[1] + 1]
                right_group.left = stone[1]
                check[stone[1]] = right_group
                max_len = max(max_len, right_group.right - right_group.left + 1)
            
            else:
                new_group = group(stone[1], stone[1])
                check[stone[1]]= new_group
                max_len = max(max_len, 1)
            
            index += 1
    
    return answer


print(solution(stones, k))