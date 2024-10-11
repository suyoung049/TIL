array = [1, 1, 1, 2]
def solution(array):
    answer = 0
    my_dictionary = dict()
    for num in array:
        if num in my_dictionary:
            my_dictionary[num] += 1
        else:
            my_dictionary[num] = 1
    
    my_dictionary = sorted(my_dictionary, key=lambda x:my_dictionary[x])
    

    print(my_dictionary)
   
    # max_num1 = [0, 0]
    # max_num2 = [0, 0]
    # for key in my_dictionary:
    #     if my_dictionary[key] > max_num1[0]:
    #         max_num1 = [my_dictionary[key], key]
    #     elif my_dictionary[key] == max_num1[0]:
    #         max_num2 = [my_dictionary[key], key]
    
    # if max_num1[0] == max_num2[0]:
    #     return -1
    
    # answer = max_num1[1]
      
    # return answer

solution(array)