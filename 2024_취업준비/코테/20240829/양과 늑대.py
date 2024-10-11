from copy import deepcopy
info = [0, 0, 1, 1, 0, 1]
edges = [[0,1],[0,2],[2,3],[2,4],[1,5]]
node_dict = dict()
answer = 0

def solution(info, edges):
    global node_dict
    for parent, child in edges:
        if parent in node_dict:
            node_dict[parent].append(child)
        else:
            node_dict[parent] = [child]
    
    dfs(info, set(node_dict[0]), 1, 0)

    return answer


def dfs(info, candidate, sheep, wolf):
    
    global answer
    sheep += visit_sheep(info, candidate)
    # next_node는 전부 늑대인 것을 위의 visit_sheep 함수를 통해서 확인
    for next_node in candidate:
        # 늑대에게 잡아 먹히지 않는 경우
        if sheep - wolf > 1:
            temp = deepcopy(candidate)
            temp.remove(next_node)
            if node_dict.__contains__(next_node):
                for child in node_dict[next_node]:
                    temp.add(child)
            
            dfs(info, temp, sheep, wolf + 1)
    
    
    answer = max(answer, sheep)
          
# 노드를 타고 내려가면서 얻을 수있는 양의 개수를 구하는 함수
def visit_sheep(info, candidate):
    cnt = 0
    temp = deepcopy(candidate)
    plage = False
    for node in candidate:
        if info[node] == 0:
            plage = True
            cnt += 1
            # 후보군에서 자기 자신 제거
            temp.remove(node)
            # 만약 양인 노드의 자식 노드가 있다면 임시 리스트에 자식노드 삽입
            if node_dict.__contains__(node):
                for child in node_dict[node]:
                    temp.add(child)
    # 양인 노드의 자식 노드가 없을 경우 후보군 리셋 필요 X
    # 후보군에는 양의 노드의 자식노드와 늑대인 형제 노드가 들어 갈수 있다.
    # 재귀적으로 진행하면서 자식노드가 없을때까지 진행
    if plage:
        candidate.clear()
        for temp_node in temp:
            candidate.add(temp_node)
        cnt += visit_sheep(info, candidate)

    return cnt


print(solution(info, edges))