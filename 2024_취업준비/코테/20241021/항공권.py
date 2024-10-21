tickets = [["ICN", "D"], ["D", "ICN"], ["ICN", "B"]]
route_list = []
from copy import deepcopy
def solution(tickets):
    global route_list
    route_list = []
    length = len(tickets)
    
    # 티켓 정보를 딕셔너리로 정리
    ticket_dic = dict()
    for ticket in tickets:
        if ticket[0] not in ticket_dic:
            ticket_dic[ticket[0]] = []
        ticket_dic[ticket[0]].append(ticket[1])
    
    # 각 출발지에서의 목적지 리스트를 알파벳 순으로 정렬
    for key in ticket_dic.keys():
        ticket_dic[key].sort()
    
    # DFS 시작
    dfs(ticket_dic, "ICN", ["ICN"], length)
    
    # 경로 중 가장 빠른 경로 반환
    return route_list[0]

def dfs(ticket_dict, current, route, remaining_tickets):
    global route_list
    
    # 종료 조건: 모든 티켓을 사용했을 때
    if remaining_tickets == 0:
        route_list.append(route[:])  # 현재 경로를 복사해서 저장
        return True
    
    # 가능한 다음 목적지 확인
    if current in ticket_dict:
        for idx, next in enumerate(ticket_dict[current]):
            # 티켓을 사용한 후 다시 복구하는 방식으로 상태 관리
            ticket_dict[current].pop(idx)
            route.append(next)
            
            # 재귀 호출
            dfs(ticket_dict, next, route, remaining_tickets - 1)

            # 상태 복구
            route.pop()
            ticket_dict[current].insert(idx, next)
            
print(solution(tickets))