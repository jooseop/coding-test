from heapq import heappush, heappop, heapify
def solution(operations):
    heap = []
    for op in operations:
        
        if op[0] == 'I':
            heappush(heap, int(op[2:]))
        else:
            # print(len(op))
            if len(heap) == 0:
                continue
            elif len(op) == 3:
                heap = [-i for i in heap]
                # 윗 줄에서 리스트를 다시 만들때, 힙이 아니기떄문에 heapify를 다시 한번더 해줌
                heapify(heap)
                heappop(heap)
                
                heap = [-i for i in heap]
                # 윗 줄에서 리스트를 다시 만들때, 힙이 아니기떄문에 heapify를 다시 한번더 해줌
                heapify(heap)
            else:
                heappop(heap)
                
    return [max(heap), min(heap)] if len(heap) > 0 else [0, 0]
