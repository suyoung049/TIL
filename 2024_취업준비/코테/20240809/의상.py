clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):
    answer = 1
    cloth_dict = dict()
    for i in range(len(clothes)):
        if cloth_dict.__contains__(clothes[i][1]):
            cloth_dict[clothes[i][1]].append(clothes[i][0])          
        else:
            cloth_dict[clothes[i][1]] = [clothes[i][0]]    
    for key in cloth_dict:
        # 의상을 선택하지 않는 경우도 생각
        answer *= len(cloth_dict[key]) + 1
    

    return answer - 1

solution(clothes)