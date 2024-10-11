files = ["ABC12", "AbC12", "abc123defg123.jpg"]

def solution(files):
    answer = []
    split_li = [[] for _ in range(len(files))]
    sign_li = ["-", " ", "."]

    for i in range(len(files)):
        head = ""
        number = ""
        for j in range(len(files[i])):
            if files[i][j].isalpha() or files[i][j] in sign_li:
                head += files[i][j]
                if number:
                    split_li[i].append(int(number))
                    number = ""
                    break
            elif not files[i][j].isalpha() and not files[i][j] in sign_li:
                if head:
                  split_li[i].append(head.lower())
                  head = ""
                number += files[i][j]
        if number:
            split_li[i].append(int(number))
        split_li[i].append(i)  

    
    sort_list = sorted(split_li, key=lambda x:(x[0], x[1], x[2]))
  
    for i in range(len(sort_list)):
        answer.append(files[sort_list[i][2]])
    
    
    return answer

print(solution(files))