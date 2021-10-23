from collections import deque
def solution(enter, leave):
    answer = [0] * len(enter)
    leave = deque(leave)
    l = leave.popleft()
    room = []
    
    for e in enter:
        room.append(e)
        
        if len(room) >= 2:
            for r in room[:-1]:
                answer[r - 1] += 1
            answer[room[-1] - 1] += len(room) - 1

        while l in room:
            room.remove(l)
            if leave:
                l = leave.popleft()

    return answer
