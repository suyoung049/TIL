s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
s = s[:-2].replace('{','').replace(',', ' ').split('}')
answer = []


s = [i.split() for i in s]

# for i,v in enumerate(s):
#     s[i] = v.split()


s.sort(key=lambda x:len(x)) 
print(s)

for tup in s:
    diff = set(tup) - set(answer)
    answer.append(list(diff)[0])


answer = list(map(int, answer))

print(answer)