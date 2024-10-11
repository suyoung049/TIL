enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

class Node:
    def __init__(self, parent):
        # 판매 금액
        self.sell_amount = 0
        # 자식 노드를 찾아가는게 아니라 부모노드를 찾아가야 하므로 부모노드 지정
        self.parent = parent
    
    def divide(self, money):
        # 분배해야할 금액
        divide_amount = money // 10
        # 자신의 이익금액 합치기
        self.sell_amount += money - divide_amount
        if divide_amount > 0 and self.parent:
            # 부모노드에 분배 금액 전달
            self.parent.divide(divide_amount)

def solution(enroll, referral, seller, amount):
    answer = []
    center = Node(None)
    node_dict = dict()
    node_dict['-'] = center
    n = len(enroll)
    for i in range(n):
        person = enroll[i]
        parent = referral[i]
        # 노드 생성 할때 부모 노드를 주기 위해서 노드를 딕셔너리로 해시
        node = Node(node_dict[parent])
        node_dict[person] = node

    # 이제 돈의 분배
    m = len(seller)

    for j in range(m):
        sell_person = seller[j]
        total_amount = amount[j] * 100

        node_dict[sell_person].divide(total_amount)
        
    for key in node_dict:
        if key == '-':
            continue
        else:
            answer.append(node_dict[key].sell_amount)
         
    return answer


solution(enroll, referral, seller, amount)