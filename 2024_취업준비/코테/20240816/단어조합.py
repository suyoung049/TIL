from itertools import permutations
spell, dic = ["p", "o", "s"], 	["sod", "eocd", "qixm", "adio", "soo"]

def solution(spell, dic):
    answer = 2
    word_list = []
    for i in permutations(spell, len(spell)):
        word = ""
        for str in i:
            word += str
        word_list.append(word)
    for text in word_list:
        if (dic.__contains__(text)):
            answer = 1
    return answer

solution(spell, dic)