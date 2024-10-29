edges =  [[2, 3], [4, 3], [1, 1], [2, 1]]
def solution(edges):
    answer = []
    node_dic = dict()
    
    # 각 노드의 나가는 간선과 들어오는 간선 수를 기록
    for edg in edges:
        if edg[0] in node_dic:
            node_dic[edg[0]][0] += 1
        else:
            node_dic[edg[0]] = [1, 0]
        if edg[1] in node_dic:
            node_dic[edg[1]][1] += 1
        else:
            node_dic[edg[1]] = [0, 1]

    
    # 결과 리스트 초기화: [센터 노드, 도넛, 막대, 8자]
    answer = [0, 0, 0, 0]
    
    # 조건에 따라 분류
    for key in node_dic:
        out_count, in_count = node_dic[key]

        # 막대 노드: 나가는 간선이 없는 노드
        if out_count == 0:
            answer[2] += 1
        
        # 8자 형태 노드: 나가는 간선과 들어오는 간선이 모두 2개인 노드
        elif out_count == 2:
            if in_count != 0:
                answer[3] += 1
            else:
                answer[0] = key
        elif out_count > 2:
            answer[0]= key

    # 도넛 수 계산: 센터 노드의 나가는 간선 수에서 막대와 8자 개수를 제외
    answer[1] = node_dic[answer[0]][0] - answer[2] - answer[3]
    
    return answer


print(solution(edges))