enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]



#판매 금액의 분배에 부모 노드를 찾아가야 하므로 부모노드를 인자로 받는 노드 객체 생성
class Node:
    def __init__(self, parent):
        self.sell_amount = 0
        self.parent = parent
    
    def divide(self, amount:int):
        # 분배 금액은 1원 단위
        divide_amount = amount//10
        self.sell_amount += amount - divide_amount
        # 분배금액이 1원 이상이라면 부모 노드에게 전달
        if divide_amount > 0 and self.parent:
            self.parent.divide(divide_amount)

def solution(enroll, referral, seller, amount):
    # 센터는 입력값에 enroll 값에 포함되지 않기 때문에 먼저 생성
    # 센터는 부모 노드가 없기 때문에 부모노드 없이 생성
    center = Node(None)
    # 판매자를 찾기 위해서 노드들 딕셔너리로 관리
    node_dict = dict()
    node_dict['-'] = center
    n = len(enroll)

    # enroll 값을 순회하면서 부모노드를 인자로 주는 노드들 생성
    # a의 enroll 순서가 referral 보다 먼저라는게 보장되어 있기 때문에 가능
    for j in range(n):
        person = enroll[j]
        parent = referral[j]
        node = Node(node_dict[parent])
        node_dict[person] = node
    
    m = len(seller)
    # 판매 금액 분배
    for i in range(m):
        sell_amount = amount[i] * 100
        sell_person = seller[i]
        node_dict[sell_person].divide(sell_amount)
    answer = []
    for key in node_dict:
        if key == "-":
            continue
        
        answer.append(node_dict[key].sell_amount)

    return answer

solution(enroll, referral, seller, amount)