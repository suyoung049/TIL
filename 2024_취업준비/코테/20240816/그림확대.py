picture, k = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2

def solution(picture, k):
    answer = []
    for line in picture:
        enl_line = ""
        for pixel in line:
            enl_line += pixel * k
        for _ in range(k):
            answer.append(enl_line)
    
    return answer


solution(picture, k)