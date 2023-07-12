import sys

sys.stdin = open("35_input.txt", "r")

lenth = []
for _ in range(9):
    lenth.append(int(input()))

lenth_sum = sum(lenth)
no_dwarf_1 = 0
no_dwarf_1 = 0

for i in range(8):
    for j in range(i+1, 9):
        if lenth_sum - lenth[i] - lenth[j] == 100:
            no_dwarf_1 = lenth[i]
            no_dwarf_2 = lenth[j]
lenth.remove(no_dwarf_1)
lenth.remove(no_dwarf_2)
sor_lenth = sorted(lenth)
for i in sor_lenth:
    print(i)