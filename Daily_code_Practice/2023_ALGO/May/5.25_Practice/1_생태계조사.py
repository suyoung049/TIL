import sys
sys.stdin = open("1_input.txt", "r")


tree_dic = {}
cnt = 0

while True:
    try:
        cnt += 1
        tree = input()
        if tree in tree_dic:
            tree_dic[tree] += 1
        else:
            tree_dic[tree] = 1
    except EOFError:
        break


tree_sor = dict(sorted(tree_dic.items(), key = lambda x : (x[0], x[1])))

for tree in tree_sor:
    print(tree, format((tree_sor[tree]/(cnt-1)*100), ".4f"))