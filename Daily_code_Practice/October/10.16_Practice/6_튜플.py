s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = s[:-2].replace('{','').replace(',', ' ').split('}')
answer = []

s = [i.split() for i in s]
# for i,v in enumerate(s):
#     s[i] = v.split()


s.sort(key=lambda x:len(x)) 

for tup in s:
    diff = set(tup) - set(answer)
    answer.append(list(diff)[0])


answer = list(map(int, answer))

print(answer)