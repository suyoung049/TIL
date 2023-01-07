today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# 날짜 문제 연산으로 생각하기 

today = list(map(int, today.split('.')))
answer = []

dic = {}

for t in terms:
    t = list(t.split(' '))
    dic[t[0]] = int(t[1])


for i in range(len(privacies)):
    pri = list(privacies[i].split(' '))
    pri_d = list(map(int, pri[0].split('.')))
    yy, mm, dd = pri_d[0], pri_d[1], pri_d[2]


    a = today[0] - yy
    b = today[1] - mm
    c = today[2] - dd

    result = (a * 12 + b - dic[pri[1]]) * 28 + c

    if result >= 0:
        answer.append(i+1)

print(answer)
    
    
    