import re

new_id = "=.="

new_id = new_id.lower()

new_id = re.sub(r'[^\w\s\.\-\_]', '', new_id)  # 제거된 문자열 출력
# re.sub  

# new_id = re.sub(r'[\w\s\.\-\_]', '', new_id)  # 제거된 문자 출력

new_id = list(new_id)

cun_ = 0

for i in range(len(new_id)):
    if new_id[i] == '.' and cun_ == 0:
        cun_ += 1

    elif new_id[i] == '.' and cun_ > 0:
        new_id[i] =''
        cun_ += 1

    elif new_id[i] != '.':
        cun_ = 0

new_id = ''.join(new_id)

print(new_id)
if new_id[0] == '.':
    start = 1
else:
    start = 0

if new_id[-1] == '.':
    new_id = new_id[start:-1]
    
else:
    new_id = new_id[start:]

# 처음과 끝을 제거 순차적으로 제거하는 것이 아니라 동시에 제거 


if len(new_id) == 0:
    new_id = 'a'

if len(new_id) >= 16:
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:14]


if len(new_id) < 3:
    while True:
        new_id += new_id[-1]

        if len(new_id) >= 3:
            break

print(new_id)