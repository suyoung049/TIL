today = "2020.01.01"
terms = ["Z 3","D 5"]
privacies = ["2019.01.01 D",
            "2019.11.15 Z",
            "2019.08.02 D",
            "2019.07.01 D",
            "2018.12.28 Z"]

term_x = {}
result = []

for i in range(len(terms)):
    y = terms[i].split()
    x = int(y[1])*28
    term_x[y[0]] = x

for pri in privacies:
    pri_x = pri.split()
    k = pri_x[0].split('.')
    yy = int(k[0])
    mm = int(k[1])
    dd = int(k[2])


    for term in terms:
        if pri_x[1] == term[0]:
            day = term_x[term[0]]

            dd = (dd + (day%336)%28) - 1 
            if dd > 28:
                dd = dd-28
                mm = mm +1
            
            if dd == 0:
                dd = 28
                mm = mm -1

            
            mm = mm + (day%336)//28
            if mm > 12:
                mm = mm -12
                yy = yy + 1
            
            yy = yy + day//336
           

            
            result.append((yy,mm,dd))

today = today.split('.')
answer = []

for i in range(len(result)):
    if result[i][0] < int(today[0]):
        answer.append(i+1)
    elif result[i][1] < int(today[1]):
        answer.append(i+1)
    elif result[i][2] < int(today[2]):
        answer.append(i+1)
answer.sort()
print(result)
print(answer)
print(12*28)

    



