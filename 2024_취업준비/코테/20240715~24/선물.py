friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

def solution(friends, gifts):
    answer = 0
    gift_list, gift_point = makeGraph(friends, gifts)
    result = gift_count(gift_list, gift_point)
    answer = max(result)
    return answer

# 그래프 만드는 함수
def makeGraph(friends, gifts):
    gift_point = [[0 for j in range(2)] for i in range(len(friends))]
    arr = [[0 for j in range(len(friends))] for i in range(len(friends))]
    for str in gifts:
        people = str.split(" ")
        give = friends.index(people[0])
        have = friends.index(people[1])
        arr[give][have] += 1
        gift_point[give][0] += 1
        gift_point[have][1] += 1
    
    return arr, gift_point

# 선물 비교 후 받은 선물 카운팅
def gift_count(gift_list, gift_pint):
    gift_count = [0 for j in range(len(friends))]
    for j in range(len(friends)):
        for i in range(j+1, len(friends)):
            if gift_list[j][i] > gift_list[i][j]:
                gift_count[j] += 1
            elif gift_list[j][i] < gift_list[i][j]:
                gift_count[i] += 1
            elif gift_list[j][i] == gift_list[i][j]:
                
                j_point = (gift_pint[j][0] - gift_pint[j][1])
                i_point = (gift_pint[i][0] - gift_pint[i][1])

                if j_point > i_point:
                    gift_count[j] += 1
                elif j_point < i_point:
                    gift_count[i] += 1
                 
    return gift_count
                
solution(friends, gifts)