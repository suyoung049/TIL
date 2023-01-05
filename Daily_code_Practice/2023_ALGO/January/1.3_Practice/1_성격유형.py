survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0 }

for i in range(len(choices)):
    if choices[i] > 4:
        score[survey[i][1]] += choices[i] - 4
    
    elif choices[i] < 4:
        score[survey[i][0]] += 4 - choices[i]

result =''

if score["R"] >= score["T"]:
    result += "R"
else:
    result += "T"

if score["C"] >= score["F"]:
    result += "C"

else:
    result += "F"

if score["J"] >= score["M"]:
    result += "J"
else:
    result += "M"

if score["A"] >= score["N"]:
    result += "A"
else:
    result += "N"

print(result)