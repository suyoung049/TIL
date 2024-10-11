my_string, queries = "rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]
def solution(my_string, queries):
    answer = ''
    for query in queries:
        sl = (my_string[query[0] : query[1]+1])
        re = "".join(reversed(sl))
        my_string = my_string[0:query[0]] + re + my_string[query[1]+1:]
    
    answer = my_string
        
    return answer


solution(my_string, queries)