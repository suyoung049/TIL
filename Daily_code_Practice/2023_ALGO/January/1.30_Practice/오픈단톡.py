record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

chat = {}
result = []

for i in record:
    ka = i.split(' ')
    if ka[0] == 'Enter':
        chat[ka[1]] = ka[2]
    elif ka[0] == 'Change':
        chat[ka[1]] = ka[2]


for i in record:
    ka = i.split(' ')
    if ka[0] == 'Enter':
        result.append(chat[ka[1]] + '님이 들어왔습니다.')
    elif ka[0] == 'Leave':
        result.append(chat[ka[1]] + '님이 나갔습니다.')




