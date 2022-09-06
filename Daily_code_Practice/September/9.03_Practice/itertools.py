import itertools
text = ['a','b','c','d','e']
qw = []
for i in range(2, 5):
    for j in itertools.combinations(text, 2):
        qw.append(j)
print(qw)