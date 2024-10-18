begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque
def solution(begin, target, words):
    len_words = len(words)
    visit = [False for _ in range(len_words)]
    queue = deque([(begin,0)])

    while queue:
        text, cnt = queue.popleft()
        if text == target:
            return cnt
        
        for i in range(len_words):
            if not visit[i]:
                if check_word(text, words[i]):
                    queue.append((words[i], cnt + 1))
                    visit[i] = True
                

    return 0

def check_word(origin, change):
    count = 0
    for i, ch in enumerate(origin):
        if ch != change[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

print(solution(begin, target, words))