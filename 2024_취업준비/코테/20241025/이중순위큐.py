
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

from heapq import heappush, heappop
from collections import Counter

def solution(operations):
    min_queue = []
    max_queue = []
    count = Counter()

    for operation in operations:
        command, num = operation.split(" ")
        num = int(num)

        if command == "I":
            heappush(min_queue, num)
            heappush(max_queue, -num)
            count[num] += 1

        elif command == "D":
            if num == 1:
                while max_queue and count[-max_queue[0]] == 0:
                    heappop(max_queue)
                if max_queue:
                    max_val = -heappop(max_queue)
                    count[max_val] -= 1

            elif num == -1:
                while min_queue and count[min_queue[0]] == 0:
                    heappop(min_queue)
                if min_queue:
                    min_val = heappop(min_queue)
                    count[min_val] -= 1

    # 최종적으로 남아 있는 값 찾기
    while min_queue and count[min_queue[0]] == 0:
        heappop(min_queue)
    while max_queue and count[-max_queue[0]] == 0:
        heappop(max_queue)

    if not min_queue or not max_queue:
        return [0, 0]
    else:
        return [-heappop(max_queue), heappop(min_queue)]


solution(operations)