# sum을 쓰면 시간초과 생김 (https://programmers.co.kr/questions/17267)
from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    queue[-1] = truck_weights[0]
    time, index = 1, 1
    total = truck_weights[0]
    
    while total > 0:
        total -= queue[0]
        queue.popleft()
        
        if index < len(truck_weights) and total + truck_weights[index] <= weight:
            queue.append(truck_weights[index])
            total += truck_weights[index]
            index += 1
        else:
            queue.append(0)
        time += 1
        
    return time
