from collections import deque
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
speak = ["aya", "ye", "woo", "ma"]
stack = ''
count = 0

for chr_ in babbling:
    chr_ = deque(chr_)
    while True:
        c = chr_.popleft()
        stack += c
        if stack in speak:
            stack = ''
        
        if len(chr_) == 0:
            if stack == '':
                count += 1
                break
            else:
                stack = ''
                break
print(count)



      
        
