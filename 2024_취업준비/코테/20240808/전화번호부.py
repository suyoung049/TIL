phone_book = ["119", "97674223", "1195524421"]
def solution(phone_book):
    prefix_set = set()
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)):
        length = len(phone_book[i])
        for j in range(1, length):
            if (prefix_set.__contains__(phone_book[i][:j])):
                answer = False
        prefix_set.add(phone_book[i])
    
    return answer


solution(phone_book)