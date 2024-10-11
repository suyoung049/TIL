inStrs = ["0123456789","9876543210","9999999999999"]
k, s, l = 50000, 5, 5
def solution(intStrs, k, s, l):
    answer = []
    for num in inStrs:
        sl_num = num[s:s+l]
        if (int(sl_num) > k):
            answer.append(sl_num)
    return answer

solution(inStrs, k, s, l)