from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer = ''

p_dict = Counter(participant)
c_dict = Counter(completion)

for win in p_dict:
    if p_dict[win] != c_dict[win]:
        answer += win
print(answer)


        