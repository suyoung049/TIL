import sys
sys.stdin = open("1_input.txt", 'r')

text = list(input().strip())


n = int(input())

text_length = len(text)
idx = text_length


test = []
for i in range(n):
    command = input().split()
    
    if command[0] == 'L':
        if idx == 0:
            continue
        else:
            idx -= 1

    elif command[0] == 'D':
        if idx == text_length-1:
            continue
        else:
            idx += 1

    elif command[0] == "P":
        temp_1 = text[:idx]
        temp_2 = text[idx:text_length]
        temp_1.append(command[1])
        text = temp_1 + temp_2
        text_length += 1
        idx +=1
        

    else:
        if idx == 0:
            continue
        else:
            temp_1 = text[:idx]
            temp_2 = text[idx:text_length]
            temp_1.pop()
            text = temp_1 + temp_2 
            text_length -= 1
            idx -= 1

answer = ""
for i in text:
    answer += i

print(answer)