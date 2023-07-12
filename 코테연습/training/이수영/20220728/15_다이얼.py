text = input()
dial = []
for i in range(len(text)):
    if text[i] in ['A','B','C']:
        dial.append('3')
    elif text[i] in ['D', 'E', 'F']:
        dial.append('4')
    elif text[i] in ['G', 'H', 'I']:
        dial.append('5')
    elif text[i] in ['J', 'K', 'L']:
        dial.append('6')
    elif text[i] in ['M', 'N', 'O']:
        dial.append('7')
    elif text[i] in ['P', 'Q', 'R', 'S']:
        dial.append('8')
    elif text[i] in ['T', 'U', 'V']:
        dial.append('9')
    elif text[i] in ['W', 'X', 'Y', 'Z']:
        dial.append('10')
    else:
        dial.append('2')
dial = list(map(int, dial))
print(sum(dial))
