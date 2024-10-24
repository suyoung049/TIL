word = "I"

answer = 0
cnt = -1
def solution(word):
    alphabet = ["A", "E", "I", "O", "U"]
    make_word = []

    dfs(alphabet, 0, make_word, word)

    return answer

def dfs(alphabet, length, make_word, word):
    global cnt
    global answer
    cnt += 1
    result = ""
    for char in make_word:
        result += char
    
    if result == word:
        answer = cnt

    if length == 5:
        return
    
    for i in range(len(alphabet)):
        make_word.append(alphabet[i])
        dfs(alphabet, length +1, make_word, word)
        make_word.pop()
        

print(solution(word))