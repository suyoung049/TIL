num_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]	
def solution(num_list):
    answer = []
    sort_list = sorted(num_list)
    answer = sort_list[5:]
    print(answer)
  
    return answer

solution(num_list)