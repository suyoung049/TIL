import itertools
from collections import Counter
# text = ['a','b','c','d','e']
# qw = []

# for j in itertools.combinations(text, 5):
#         qw.append(j)
# print(qw)

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
cource = [2,3,5]

answer = []


for i in cource:
    result = []      # 필요한 세트메뉴의 수 만큼 결과값 리셋
    for j in orders:

        for k in itertools.combinations(sorted(j), i):  # 조합을 출력하는 메서드  # sort로 정렬해야 순서가 바껴도 같은 세트메뉴로 인식
            result.append(''.join(k))  # 조합값은 메뉴하나하나 따로 출력되기 때문에 join으로 합쳐주기
    
    print(result)
    menue = Counter(result)    # 카운터 메서드로 세트메뉴가 몇번 주문 되었는지 딕셔너리 형식으로 저장해주는 메서드
    print(menue)
    if len(menue) > 0:          

        max_ = max(list(menue.values()))  # 가장 많이 주문된 세트 메뉴 구하기

        if max_ >= 2:
            for k, v  in menue.items():  
                if v == max_:            
                    answer.append(k)      # 가장 많이 주문된 세트메뉴가 2개이상이어도 동시 출력

answer.sort()  # 세트메뉴도 알파벳순으로 오름 차순 
print(answer)


        


         
