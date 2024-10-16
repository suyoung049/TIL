from collections import deque
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
def solution(n, edge):
    edge_dic = dict()
    check = [False for _ in range(n+1)]

    for node in edge:
        if edge_dic.__contains__(node[0]):
            edge_dic[node[0]].append(node[1])
        else:
            edge_dic[node[0]] = [node[1]]
        
        if edge_dic.__contains__(node[1]):
            edge_dic[node[1]].append(node[0])
        else:
            edge_dic[node[1]] = [node[0]]
    
    cnt_list = bfs(edge_dic, check)
    max_cnt = max(cnt_list)
    answer = 0
    for cnt in cnt_list:
        if cnt == max_cnt:
            answer += 1
    return answer

def bfs(edge_dict, check):
    cnt_list = []
    queue = deque([(1, 0)])
    check[1] = True

    while queue:
        node = queue.popleft()
        edge, cnt = node[0], node[1]

        for idx in edge_dict[edge]:
            if not check[idx]:
                check[idx] = True
                queue.append((idx, cnt + 1))
                cnt_list.append(cnt + 1)
    
    return cnt_list
print(solution(n, edge))