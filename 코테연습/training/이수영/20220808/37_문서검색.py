import sys

sys.stdin = open("37_input.txt", "r")
coun = 0
text = input()
surch = input()
index = 0
while index <= len(text) - len(surch):
    if text[index : index + len(surch)] == surch:
        coun += 1
        index += len(surch)
    else:
        index += 1

print(coun)


