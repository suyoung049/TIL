s = "pPoooyY"

s = s.lower()

p_con = s.count('p')
s_con = s.count('y')

if p_con == s_con:
    print('true')

else:
    print('false')