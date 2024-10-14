alp, cop = 10, 1
problems = [[1, 1, 1, 1, 1], [5, 5, 1, 1, 3]]

def solution(alp, cop, problems):
    answer = 0
    max_alq = max([alp_req for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems])
    max_coq = max([cop_req for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems])
    
    if alp >= max_alq and cop >= max_coq:
        return 0

    # 요구 되는 포인트의 최대값 구하기
    # ex 2, 3이 주어지고 요구 사항이 1, 4라면 최대 요구 사항은 2, 4 이다(능력은 증가만 가능)
    max_alq = max(max_alq, alp)
    max_coq = max(max_coq, cop)
   

    # 알고력과 코딩력을 높이기 위해 공부하는 것을 문제 푸는 것과 같게 치한
    # 문제들에 공부하는 것을 같이 포함
    # 알고력 공부
    problems.append([0, 0, 1, 0, 1])
    # 코딩력 공부
    problems.append([0, 0, 0, 1, 1])

    # 각 문제에 도달하는 최소 시간을 dp로 기록하고 갱신
    # ex) dp[3][2] 의 경우 알고력 3, 코딩력 2의 문제를 풀수 있는 최소시간
    dp = [[float('inf') for i in range(max_coq + 1)] for j in range(max_alq + 1)]
    dp[alp][cop] = 0
    

    # 최소값을 구해야 하니깐 공부만 해서 최대포인트에 도달하느 시간 까지 완전 탐색
    for j in range(alp, max_alq + 1):
        for i in range(cop, max_coq + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if j < alp_req or i < cop_req:
                    continue
                nj = j + alp_rwd
                ni = i + cop_rwd
                # 최대 요구의 문제를 풀기만 하면 되기 때문에 넘어가는것도 최대 요구로 수정
                if nj > max_alq:
                    nj = max_alq
                if ni > max_coq:
                    ni = max_coq
                # 문제를 못풀면 의미가 없음
                dp[nj][ni] = min(dp[nj][ni], dp[j][i] + cost)
    
    return dp[-1][-1]

print(solution(alp, cop, problems))