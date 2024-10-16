bridge_length = 100
weight = 100
truck_weights = [10]
from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 트럭의 이동거리
    bridge = deque([ 0 for _ in range(bridge_length)])
    time = 0
    bridge_weight = 0


    deque_truck = deque(truck_weights)
    time = 0

    while bridge:
        first = bridge.popleft()
        bridge_weight -= first
        time += 1
        if deque_truck:
            if bridge_weight + deque_truck[0] <= weight:
                left = deque_truck.popleft()
                bridge.append(left)
                bridge_weight += left
            else:
                bridge.append(0)
        
    return time


print(solution(bridge_length, weight, truck_weights))