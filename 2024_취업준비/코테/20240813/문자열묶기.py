strArr = ["a","bc","d","efg","hi"]
def solution(strArr):
    answer = -1
    len_dict = dict()
    for str in strArr:
      if len_dict.__contains__(len(str)):
         len_dict[len(str)] += 1
      else:
         len_dict[len(str)] = 1

    for key in len_dict:
       if answer < len_dict[key]:
          answer = len_dict[key]
    
    return answer

solution(strArr)