import sys

sys.stdin = open("10769_input.txt", "r")
text = input()
h_coun = text.count(':-)')
s_coun = text.count(':-(')

if h_coun > s_coun:
    print('happy')
elif h_coun < s_coun:
    print('sad')
elif h_coun == 0 and s_coun == 0:
    print('none')
elif h_coun == s_coun:
    print('unsure')
