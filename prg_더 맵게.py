# solution1
from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
            answer += 1
        except:
            return -1

    return answer


# solution2
from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        answer += 1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer
